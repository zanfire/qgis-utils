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

    def create_dialog(self): 
        return ComputeCompactRatioDialog() 

    def initialize(self):
        self.input_layer = layer_helper.get_layer(self.dlg.input_layer_name())
        self.volumes_layer = layer_helper.create_layer(self.dlg.volumes_layer_name(), LAYER_VOLUMES_FIELDS, self.input_layer, 'Polygon', False)
        self.building_layer = layer_helper.create_layer(self.dlg.building_layer_name(), LAYER_BUILDING_FIELD, self.input_layer, 'Polygon', False)


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
            print(type(g))
            feature.setGeometry(QgsGeometry(g))
            #feature.setGeometry(QgsGeometry(layer_helper.copy_geometry(f)))
            #feature[FIELD_ID_CADASTRE] = f[FIELD_CODCAT] 
            feature[FIELD_HEIGHT] = f[FIELD_VOLUME_HEIGHT] 
            feature[FIELD_AREA_GROSS] = g.area()
            feature[FIELD_VOL_GROSS] = feature[FIELD_HEIGHT] * feature[FIELD_AREA_GROSS]
            feature[FIELD_WALL_SURF] = g.length()
            feature[FIELD_DISP_SURF] = mem.disperding_surface(index, g, features_id, feature[FIELD_HEIGHT]) 
            #feature[FIELD_AREA_R] =
            #feature[FIELD_AREA_NET] =
            #feature[FIELD_VOL_R] =
            #feature[FIELD_VOL_NET] =
            #feature[FIELD_LEVEL_H] =
            #feature[FIELD_N_LEVEL] =
            #feature[FIELD_FLOOR_AREA] =
            
            #feature[FIELD_TYPE_USAGE] = f[FIELD_CADASTRE_USAGE]
            result.append(feature)
            id_cadastre = f[FIELD_CODCAT]
            if not id_cadastre in map_cadastre_building.keys():
                map_cadastre_building[id_cadastre] = [ feature ]
            else:
                map_cadastre_building[id_cadastre].append(feature)

        return result

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

        #if self.dlg.create_intersection_layer_check():
        #    self.create_intersection_layer(self.layer, index, features_id)
        t3 = time.clock() 
        print("Performance t1 " + str(t2 - t1) + ", t2 " + str(t3 - t2))
        
    
    def compute_building(self, progress, map_cadastre_building):
        #features_id = layer_helper.load_features(l)
        #index = layer_helper.build_spatialindex(features_id.values())
 
        result = []
        count = 0
        count_max = len(map_cadastre_building.keys())
        for cadastre in map_cadastre_building.keys():
            count += 1
            progress.emit(50 + int(count * (50.0 / count_max)))  
            features_temp = [ ]
            idx = 0
            for f in map_cadastre_building[cadastre]:
                insert = True
                (geom, feature_set) = mem.merge(f, map_cadastre_building[cadastre])
                for fe in features_temp:
                    if geom.equals(fe.geometry()) or geom.contains(fe.geometry()):
                        insert = False
                        break
                if insert:
                    features_temp.append(QgsFeature(self.building_layer.pendingFields()))
                    features_temp[idx].setGeometry(geom)
                    id_mem = cadastre + '_' + str(idx)
                    features_temp[idx][FIELD_ID_CADASTRE] = cadastre
                    features_temp[idx][FIELD_ID_MEM] = id_mem
                    #features_temp[idx][FIELD_USE] = f[FIELD_TYPE_USAGE]
                    #features_temp[idx][FIELD_CODCAT] = f[FIELD_CATID]
                    #features_temp[idx][FIELD_ID_EPC] = ''
                    for elem in feature_set:
                        elem[FIELD_ID_MEM] = id_mem
                    idx += 1
            # We have created the final set.
            result.extend(features_temp)
#    for feature in sfeatures:
#        total_vol = 0
#        total_disp = 0
#        ids = index.intersects(feature.geometry().boundingBox())
#        for i in ids:
#            f = features[i]
#            if not feature.geometry().disjoint(f.geometry()):
#                total_vol += f[FIELD_HEIGHT] * f[FIELD_AREA]
#                total_disp += f[FIELD_DISPERSING_SURFACE]
#        mcr = total_disp / total_vol
#        feature[FIELD_COMPACT_R] = mcr
        return result

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
