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
    
    intersection_features = None

    def __init__(self, iface, menu_name):
        super(ComputeCompactRatioAction, self).__init__(iface, menu_name, "2 - Create energy layers")

    def create_dialog(self): 
        return ComputeCompactRatioDialog() 

    def initialize(self):
        self.input_layer = layer_helper.get_layer(self.dlg.input_layer_name())
        self.volumes_layer = layer_helper.create_layer(self.dlg.volumes_layer_name(), LAYER_VOLUMES_FIELDS, self.input_layer, 'Polygon', False)
        self.building_layer = layer_helper.create_layer(self.dlg.building_layer_name(), LAYER_BUILDING_FIELD, self.input_layer, 'Polygon', False)

    def compute(self, progress):
        """
        Creating final layer trough an intermediate layer.
        """
        t1 = time.clock()
        features = self.input_layer.getFeatures()
        features_id = layer_helper.load_features(self.input_layer)
        index = layer_helper.build_spatialindex(features_id.values())
        map_cadastre_building = {}
        self.volumes_features = self.compute_volumes(progress, features, index, features_id, map_cadastre_building)
        t2 = time.clock()
        self.building_features = self.compute_building(progress, map_cadastre_building)
        if self.dlg.create_intersection_layer_check():
            self.create_intersection_layer(index, features_id)
        t3 = time.clock() 
        QgsMessageLog.logMessage("Performance t1 " + str(t2 - t1) + ", t2 " + str(t3 - t2))

    def compute_volumes(self, progress, features, index, features_id, map_cadastre_building):
        result = []
        # Filling working/temporary layer.
        count = 0
        count_max = len(features_id.values())
        for f in features:
            count += 1
            progress.emit(int(count * (50.0 / count_max)))  
            feature = QgsFeature(self.volumes_layer.pendingFields())
            g = f.geometry()
            feature.setGeometry(QgsGeometry(g))
            #feature.setGeometry(QgsGeometry(layer_helper.copy_geometry(f)))
            feature[FIELD_ID_CADASTRE] = f[FIELD_CODCAT] 
            feature[FIELD_USE] = f[FIELD_CADASTRE_USAGE] 
            feature[FIELD_HEIGHT] = f[FIELD_VOLUME_HEIGHT] 
            feature[FIELD_AREA_GROSS] = g.area()
            feature[FIELD_VOL_GROSS] = feature[FIELD_HEIGHT] * feature[FIELD_AREA_GROSS]
            feature[FIELD_WALL_SURF] = mem.compute_external_wall_surface(index, g, features_id, feature[FIELD_HEIGHT])
            feature[FIELD_DISP_SURF] = feature[FIELD_AREA_GROSS] * 2 + feature[FIELD_WALL_SURF]
            #feature[FIELD_AREA_R] =
            #feature[FIELD_AREA_NET] =
            #feature[FIELD_VOL_R] =
            #feature[FIELD_VOL_NET] =
            #feature[FIELD_H_LEVEL] =
            #feature[FIELD_N_LEVEL] =
            #feature[FIELD_FLOOR_AREA] =
            
            result.append(feature)
            # Create map cadastre to features for next steps.
            id_cadastre = feature[FIELD_USE] + '-' + f[FIELD_CODCAT]
            if not id_cadastre in map_cadastre_building.keys():
                map_cadastre_building[id_cadastre] = [ feature ]
            else:
                map_cadastre_building[id_cadastre].append(feature)
        return result

        
    
    def compute_building(self, progress, map_cadastre_building):
        #features_id = layer_helper.load_features(l)
        #index = layer_helper.build_spatialindex(features_id.values())
 
        result = []
        count = 0
        count_max = len(map_cadastre_building.keys())
        for key in map_cadastre_building.keys():
            count += 1
            progress.emit(50 + int(count * (50.0 / count_max)))  
            features_temp = [ ]
            idx = 0
            for f in map_cadastre_building[key]:
                insert = True
                (geom, feature_set) = mem.merge(f, map_cadastre_building[key])
                for fe in features_temp:
                    if not geom.disjoint(fe.geometry()) or geom.equals(fe.geometry()) or geom.contains(fe.geometry()) or geom.within(fe.geometry()):
                        insert = False
                        break
                if insert:
                    feature = QgsFeature(self.building_layer.pendingFields())
                    features_temp.append(feature);
                    feature.setGeometry(geom)
                    id_mem = key + '_' + str(idx)
                    feature[FIELD_ID_CADASTRE] = '-'.join(key.split('-')[1:])
                    feature[FIELD_ID_MEM] = id_mem
                    feature[FIELD_USE] = f[FIELD_USE]
                    #features_temp[idx][FIELD_USE] = f[FIELD_TYPE_USAGE]
                    #features_temp[idx][FIELD_CODCAT] = f[FIELD_CATID]
                    #features_temp[idx][FIELD_ID_EPC] = ''
                    
                    feature[FIELD_FOOT_AREA] = 0
                    feature[FIELD_VOL_GROSS] = 0
                    feature[FIELD_DISP_SURF] = 0
                    feature[FIELD_WALL_SURF] = 0
                    total_disp = 0
                    for elem in feature_set:
                        elem[FIELD_ID_MEM] = id_mem
                        feature[FIELD_FOOT_AREA] += elem[FIELD_AREA_GROSS]
                        feature[FIELD_VOL_GROSS] += elem[FIELD_VOL_GROSS]
                        feature[FIELD_DISP_SURF] += elem[FIELD_DISP_SURF]
                        feature[FIELD_WALL_SURF] += elem[FIELD_WALL_SURF]
                    if feature[FIELD_VOL_GROSS] > 0:
                        feature[FIELD_COMPACT_R] = feature[FIELD_DISP_SURF] / feature[FIELD_VOL_GROSS]
                    idx += 1
            # We have created the final set.
            result.extend(features_temp)
        return result

    def create_intersection_layer(self, index, features):
        self.intersection_layer = layer_helper.create_layer("Volumes_intersection", [], self.volumes_layer, 'LineString', False)
        new_features = []
        for f in features.values():
            g1 = f.geometry()
            ids = index.intersects(g1.boundingBox())
            for i in ids:
                g2 = features[i].geometry()
                if not g1.equals(g2):
                    intersection_set = mem.get_intersection_debug(g1, g2)
                    for intersection in intersection_set:
                        feature = QgsFeature()
                        feature.setGeometry(intersection)
                        new_features.append(feature)
        self.intersection_features = new_features

    def apply(self):
        if self.dlg.volumes_layer_path() != '':
            self.volumes_layer.startEditing()
            self.volumes_layer.dataProvider().addFeatures(self.volumes_features)
            self.volumes_layer.commitChanges()
            result = layer_helper.save_layer(self.volumes_layer, self.dlg.volumes_layer_path())
            if result == QgsVectorFileWriter.NoError:
                layer_name = self.dlg.volumes_layer_name()
                self.iface.addVectorLayer(self.dlg.volumes_layer_path(), layer_name, "ogr") 

        if self.dlg.building_layer_path() != '':
            self.building_layer.startEditing()
            self.building_layer.dataProvider().addFeatures(self.building_features)
            self.building_layer.commitChanges()
            result = layer_helper.save_layer(self.building_layer, self.dlg.building_layer_path())
            if result == QgsVectorFileWriter.NoError:
                layer_name = self.dlg.building_layer_name()
                self.iface.addVectorLayer(self.dlg.building_layer_path(), layer_name, "ogr") 
        if self.intersection_features != None:
            self.intersection_layer.startEditing()
            self.intersection_layer.dataProvider().addFeatures(self.intersection_features)
            self.intersection_layer.commitChanges()
            QgsMapLayerRegistry.instance().addMapLayer(self.intersection_layer) 
