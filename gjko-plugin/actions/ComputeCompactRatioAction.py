# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
import time

from Action import Action
from ..dialogs import ComputeCompactRatioDialog, ProgressDialog
from ..util import layer_helper
from ..DEFINES import *
from ..logic import mem

class ComputeCompactRatioAction(Action):
    """
    Compute energy efficency base value.
    """
    
    def __init__(self, iface, menu_name):
        super(ComputeCompactRatioAction, self).__init__(iface, menu_name, "Compute energy efficency values...")

    def run(self): 
        self.dlg = ComputeCompactRatioDialog() 
        self.dlg.show()
        result = self.dlg.exec_() 
        if result == 1:
            # Initialize and compute
            self.initialize(self.dlg.working_layer_name())
            self.compute()
            print("Completed.")

    def initialize(self, name):
        self.name = name
        self.volumes = layer_helper.get_layer(self.dlg.volumes_layer_name())
        self.energy_layer = layer_helper.get_layer(name)
        if self.energy_layer != None:
            # TODO: Notify user about current state.
            print("Notify user.")
        else:
            self.energy_layer = layer_helper.create_layer(name, LAYER_MEM_FINAL, self.volumes)
            self.wip_layer = layer_helper.create_layer(name + '_temporary', LAYER_MEM_INTERMEDIATE_FIELDS, self.volumes)

    def compute(self):
        """
        Creating final layer trough an intermediate layer.
        """
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))
        t1 = time.clock()
        QgsMessageLog.logMessage("Starting compation ...", "Gjko", QgsMessageLog.INFO)
        
        features = self.volumes.getFeatures()
        features_id = layer_helper.load_features(self.volumes)
        index = layer_helper.build_spatialindex(features_id.values())
        new_features = []
        features_lr = {}

        # Filling working/temporary layer.
        for f in features:
            feature = QgsFeature(self.wip_layer.pendingFields())
            feature.setGeometry(QgsGeometry(layer_helper.copy_geometry(f)))
            feature[FIELD_TYPE_USAGE] = f[FIELD_CADASTRE_USAGE]
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
        self.wip_layer.startEditing()
        self.wip_layer.dataProvider().addFeatures(new_features)
        self.wip_layer.commitChanges()
        t2 = time.clock()

        self.compute_final_layer(self.wip_layer, features_lr)

        if self.dlg.create_intersection_layer_check():
            self.create_intersection_layer(self.layer, index, features_id)
        t3 = time.clock()
        
        #
        if not self.dlg.keep_temporary_layer():
            QgsMapLayerRegistry.instance().removeMapLayer(self.wip_layer.id())
            self.wip_layer = None
        
        QApplication.restoreOverrideCursor()
        print("Performance t1 " + str(t2 - t1) + ", t2 " + str(t3 - t2))
        
        if self.dlg.location() != '':
            result = layer_helper.save_layer(self.energy_layer, self.dlg.location())
            if result == QgsVectorFileWriter.NoError:
                layer_name = self.energy_layer.name()
                QgsMapLayerRegistry.instance().removeMapLayer(self.energy_layer.id())
                self.energy_layer = self.iface.addVectorLayer(self.dlg.location(), layer_name, "ogr") 
    
    def compute_final_layer(self, l, features_lr):
        features_id = layer_helper.load_features(l)
        index = layer_helper.build_spatialindex(features_id.values())
 
        new_features = []
        for id_lr in features_lr.keys():
            feature = [ ]
            idx = 0
            features = features_lr[id_lr]
            for f in features:
                insert = True
                g = f.geometry()
                #print("Entering merge ...")
                geom = mem.merge(g, features)
                #print("Exiting merge ...")
                for fe in feature:
                    if geom.equals(fe.geometry()) or geom.contains(fe.geometry()):
                        insert = False
                        break
                if insert:
                    feature.append(QgsFeature(self.energy_layer.pendingFields()))
                    feature[idx].setGeometry(geom)
                    feature[idx][FIELD_ID_MEM] = f[FIELD_CATID] + '_' + str(idx)
                    feature[idx][FIELD_COMPACT_R] = 0.0
                    feature[idx][FIELD_USE] = f[FIELD_TYPE_USAGE]
                    feature[idx][FIELD_CODCAT] = f[FIELD_CATID]
                    feature[idx][FIELD_ID_EPC] = ''
                    idx += 1
            new_features.extend(feature)
        mem.compute_multiple_compact_ratio2(index, new_features, features_id)
        self.energy_layer.startEditing()
        self.energy_layer.dataProvider().addFeatures(new_features)
        self.energy_layer.commitChanges()

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
