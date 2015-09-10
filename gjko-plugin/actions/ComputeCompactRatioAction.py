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
        super(ComputeCompactRatioAction, self).__init__(iface, menu_name, "Compute energy efficency values...")

    def run(self): 
        self.dlg = ComputeCompactRatioDialog() 
        self.dlg.show()
        result = self.dlg.exec_() 
        if result == 1:
            volumes_layer = layer_helper.get_layer(self.dlg.volumes_layer_name())
            layer = self.initialize(self.dlg.working_layer_name(), volumes_layer)
            self.compute(layer, volumes_layer)
            print("Completed.")

    def initialize(self, name, baselayer):
        layer = layer_helper.get_layer(name)
        if layer != None:
            # Error or not?
            # Fill with needed attribute! 
            return layer
        # Check if exists layer name
        # Create layer.
        layer = layer_helper.create_layer(name, LAYER_MEM_INTERMEDIATE_FIELDS, baselayer)
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
            feature.setGeometry(QgsGeometry(layer_helper.copy_geometry(f)))
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

        #for id_lr in features_lr.keys():
        #    mem.compute_multiple_compact_ratio(features_lr[id_lr])

        QgsMessageLog.logMessage("Adding " + str(len(new_features))+" new features.", "Gjko", QgsMessageLog.INFO)
        layer.startEditing()
        layer.dataProvider().addFeatures(new_features)
        layer.commitChanges()

        if self.dlg.simplifyLayerCheck():
            self.compute_simplify(layer, features_lr)
        if self.dlg.create_intersection_layer_check():
            self.create_intersection_layer(layer, index, features_id)

    def compute_simplify(self, l, features_lr):
        features_id = layer_helper.load_features(l)
        index = layer_helper.build_spatialindex(features_id.values())
 
        layer = layer_helper.create_layer(l.name() + "_simplified", LAYER_MEM_FINAL_FIELDS, l)
        new_features = []
        for id_lr in features_lr.keys():
            feature = [ ]
            idx = 0
            features = features_lr[id_lr]
            for f in features:
                insert = True
                g = f.geometry()
                geom = mem.merge(g, features)
                for fe in feature:
                    if geom.equals(fe.geometry()) or geom.contains(fe.geometry()):
                        insert = False
                        break
                if insert:
                    feature.append(QgsFeature(layer.pendingFields()))
                    feature[idx].setGeometry(geom)
                    feature[idx][FIELD_CATID] = f[FIELD_CATID] + '_' + str(idx)
                    feature[idx][FIELD_COMPACT_RATIO] = 0.0
                    idx += 1
            new_features.extend(feature)
        mem.compute_multiple_compact_ratio2(index, new_features, features_id)
        layer.startEditing()
        layer.dataProvider().addFeatures(new_features)
        layer.commitChanges()

    def create_intersection_layer(self, l, index, features):
        layer = layer_helper.create_layer(l.name() + "_intersection", [], l, 'LineString')
        new_features = []
        for f in features.values():
            g1 = f.geometry()
            ids = index.intersects(g1.boundingBox())
            for i in ids:
                g2 = features[i].geometry()
                if not g1.equals(g2):
                    intersection_set = mem.get_intersection(g1, g2)
                    for intersection in intersection_set:
                        feature = QgsFeature()
                        feature.setGeometry(intersection)
                        new_features.append(feature)
        layer.startEditing()
        layer.dataProvider().addFeatures(new_features)
        layer.commitChanges()
