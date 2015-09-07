# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

from Action import Action
from ..dialogs import ComputeCompactRatioDialog
from ..util import layer_helper
from ..DEFINES import *
from ..logic import mem

class ComputeCompactRatioAction(Action):
    def __init__(self, iface, menu_name):
        super(ComputeCompactRatioAction, self).__init__(iface, menu_name, "Compute compact ratio")

    def run(self): 
        dlg = ComputeCompactRatioDialog() 
        dlg.show()
        result = dlg.exec_() 
        if result == 1:
            volumes_layer = layer_helper.get_layer(dlg.volumes_layer_name())
            layer = self.initialize(dlg.working_layer_name(), volumes_layer)
            self.compute(layer, volumes_layer)
        else:
            print("Cancel!")
        print("Completed.")

    def initialize(self, name, baselayer):
        layer = layer_helper.get_layer(name)
        if layer != None:
            # Error or not?
            # Fill with needed attribute! 
            return layer
        # Check if exists layer name
        # Create layer.
        layer = layer_helper.create_layer(name, LAYER_MEM_FIELDS, baselayer)
        return layer

    def compute(self, layer, volumes):
        QgsMessageLog.logMessage("Starting compation ...", "Gjko", QgsMessageLog.INFO)
        
        features = volumes.getFeatures()
        features_id = layer_helper.load_features(volumes)
        index = layer_helper.build_spatialindex(features_id.values())
        new_features = []
        features_lr = {}

        for f in features:
            QgsMessageLog.logMessage("Working on " + str(f.id())+" feature.", "Gjko", QgsMessageLog.INFO)
            feature = QgsFeature(layer.pendingFields())
            feature.setGeometry(layer_helper.copy_geometry(f))
            # Compute comapct ratio 
            mem.compute_simple_compact_ratio(f, feature)
            # Compute dispersing surface.
            mem.dispersing_surface(index, feature, features_id)
            new_features.append(feature)
            id_lr = f[FIELD_CODCAT]
            if not id_lr in features_lr.keys():
                features_lr[id_lr] = [ feature ]
            else:
                features_lr[id_lr].append(feature)
        for id_lr in features_lr.keys():
            mem.compute_multiple_compact_ratio(features_lr[id_lr])

        QgsMessageLog.logMessage("Adding " + str(len(new_features))+" new features.", "Gjko", QgsMessageLog.INFO)
        layer.startEditing()
        layer.dataProvider().addFeatures(new_features)
        layer.commitChanges()

        self.compute_simplify(layer, features_lr)

    def compute_simplify(self, l, features_lr):
        layer = layer_helper.create_layer(l.name() + "_simplified", LAYER_MEM_FIELDS, l)
        new_features = []
        for id_lr in features_lr.keys():
            feature = QgsFeature(layer.pendingFields())
            geom = None
            for f in features_lr[id_lr]:
                if geom == None:
                    geom = f.geometry()
                    #geom = layer_helper.copy_geometry(f)
                    feature[FIELD_CATID] = f[FIELD_CATID]
                    feature[FIELD_DISPERSING_SURFACE] = f[FIELD_DISPERSING_SURFACE]
                    feature[FIELD_MULTIPLE_COMPACT_RATIO] = f[FIELD_MULTIPLE_COMPACT_RATIO]
                else:
                    feature[FIELD_DISPERSING_SURFACE] += f[FIELD_DISPERSING_SURFACE]
                    geom = geom.combine(f.geometry()) 
                    #geom = geom.combine(layer_helper.copy_geometry(f)) 
            feature.setGeometry(geom)
            feature[FIELD_AREA] = geom.area()
            feature[FIELD_PERIMETER] = geom.length()
            new_features.append(feature)
        layer.startEditing()
        layer.dataProvider().addFeatures(new_features)
        layer.commitChanges()


