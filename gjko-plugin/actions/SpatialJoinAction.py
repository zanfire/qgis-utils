# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import os
import time

from Action import Action
from ..dialogs import SpatialJoinDialog
from ..util import layer_helper, reader_csv
from ..DEFINES import *
from ..logic import mem, code_generator

class SpatialJoinAction(Action):
    def __init__(self, iface, menu_name):
        super(SpatialJoinAction, self).__init__(iface, menu_name, "Spatial join...")
    
    def create_dialog(self):
        return SpatialJoinDialog() 

    def initialize(self):
        self.volumes_layer = layer_helper.get_layer(self.dlg.volumes_layer_name())
        self.cadastre_layer = layer_helper.get_layer(self.dlg.cadastre_layer_name())
        self.cadastre_terrain_layer = layer_helper.get_layer(self.dlg.cadastre_terrain_layer_name())
        self.attributes = []
        self.fields = QgsFields()
        for attr in self.volumes_layer.pendingFields():
            field = QgsField(attr.name(), attr.type())
            self.attributes.append(field)
            self.fields.append(field)
        field = QgsField(FIELD_CODCAT, QVariant.String)
        self.attributes.append(field)
        self.fields.append(field)

    def compute(self, progress):
        cadastre_features = layer_helper.load_features(self.cadastre_layer)
        index = layer_helper.build_spatialindex(cadastre_features.values())
        cadastre_terrain_features = layer_helper.load_features(self.cadastre_terrain_layer)
        index_cadastre_terrain = layer_helper.build_spatialindex(cadastre_terrain_features.values())

        self.new_features = []
        features = layer_helper.load_features(self.volumes_layer)
        count_max = len(features)
        count = 0
        for f in features.values():
            count += 1
            progress.emit(int(count * (100.0 / count_max)))  
            feature = QgsFeature(QgsFields(self.fields))
            ids = index.intersects(f.geometry().boundingBox())
            add = False
            if len(ids) == 0:
                add = False
            elif len(ids) == 1:
                add = True
                feature[FIELD_CODCAT] = cadastre_features[ids[0]][FIELD_CODCAT]
            else:
                id_max = -1
                area_max = -1
                for i in ids:
                    common = QgsGeometry(f.geometry().intersection(cadastre_features[i].geometry()))
                    if common.area() > area_max:
                        id_max = i
                        area_max = common.area()
                if id_max > -1:
                    add = True
                    feature[FIELD_CODCAT] = cadastre_features[id_max][FIELD_CODCAT]
            # Try with the cadastre terrain.
            if not add:
                # Search in cadastre terrain
                ids = index_cadastre_terrain.intersects(f.geometry().boundingBox())
                if len(ids) == 0:
                    add = False
                if len(ids) == 1:
                    add = True
                    feature[FIELD_CODCAT] = cadastre_terrain_features[ids[0]][FIELD_CADASTRE_TERRAIN_ID]
                else:
                    id_max = -1
                    area_max = -1
                    for i in ids:
                        common = QgsGeometry(f.geometry().intersection(cadastre_terrain_features[i].geometry()))
                        if common.area() > area_max:
                            id_max = i
                            area_max = common.area()
                    if id_max > -1:
                        add = True
                        feature[FIELD_CODCAT] = cadastre_terrain_features[id_max][FIELD_CADASTRE_TERRAIN_ID]
            # Final we add this feature
            if add:
                feature.setGeometry(QgsGeometry(f.geometry()))
                # Determinate cadastre ID.
                for attr in self.volumes_layer.pendingFields():
                    feature[attr.name()] = f[attr.name()]
                self.new_features.append(feature)

    def apply(self):
        self.output_layer = layer_helper.create_layer(os.path.splitext(os.path.basename(self.dlg.location()))[0], self.attributes, self.volumes_layer)
        self.output_layer.startEditing()
        self.output_layer.dataProvider().addFeatures(self.new_features)
        self.output_layer.commitChanges()
        
        if self.dlg.location() != '':
            result = layer_helper.save_layer(self.output_layer, self.dlg.location())
            if result == QgsVectorFileWriter.NoError:
                layer_name = self.output_layer.name()
                QgsMapLayerRegistry.instance().removeMapLayer(self.output_layer.id())
                self.output_layer = self.iface.addVectorLayer(self.dlg.location(), layer_name, "ogr") 
            else:
                QgsMessageLog.logMessage("Failed to save layer, error: " + str(result))
