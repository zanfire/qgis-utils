# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import os
import time

from Action import Action
from ..dialogs import SpatialJoinMaxAreaDialog
from ..util import layer_helper, reader_csv
from ..DEFINES import *
from ..logic import mem, code_generator

class SpatialJoinMaxAreaAction(Action):
    def __init__(self, iface, menu_name):
        super(SpatialJoinMaxAreaAction, self).__init__(iface, menu_name, "Spatial join max area...")
    
    def create_dialog(self):
        return SpatialJoinMaxAreaDialog() 

    def initialize(self):
        self.layer1 = layer_helper.get_layer(self.dlg.layer1_layer_name())
        self.layer2 = layer_helper.get_layer(self.dlg.layer2_layer_name())
        self.max_area_field = self.dlg.field_name()
        self.attributes = []
        self.fields = QgsFields()
        for attr in self.layer1.pendingFields():
            field = QgsField(attr.name(), attr.type())
            self.attributes.append(field)
            self.fields.append(field)
        for attr in self.layer2.pendingFields():
            if attr.name() == self.max_area_field:
                field = QgsField(attr.name(), attr.type())
                self.attributes.append(field)
                self.fields.append(field)
                break

    def compute(self, progress):
        features1 = layer_helper.load_features(self.layer1)
        features2 = layer_helper.load_features(self.layer2)
        index = layer_helper.build_spatialindex(features2.values())
        #index2 = layer_helper.build_spatialindex(features2.values())

        self.new_features = []
        features = layer_helper.load_features(self.layer1)
        count_max = len(features)
        count = 0
        for f in features.values():
            count += 1
            progress.emit(int(count * (100.0 / count_max)))  
            feature = QgsFeature(QgsFields(self.fields))
            ids = index.intersects(f.geometry().boundingBox())
            add = False
            if len(ids) == 0:
                add = True
            elif len(ids) == 1:
                add = True
                if not f.geometry().disjoint(features2[ids[0]].geometry()):
                    feature[self.max_area_field] = features2[ids[0]][self.max_area_field]
            else:
                id_max = -1
                area_max = -1
                for i in ids:
                    if not f.geometry().disjoint(features2[i].geometry()):
                        common = QgsGeometry(f.geometry().intersection(features2[i].geometry()))
                        if common.area() > area_max:
                            id_max = i
                            area_max = common.area()
                if id_max > -1:
                    add = True
                    feature[self.max_area_field] = features2[id_max][self.max_area_field]
            # Final we add this feature
            if add:
                feature.setGeometry(QgsGeometry(f.geometry()))
                # Determinate cadastre ID.
                for attr in self.layer1.pendingFields():
                    feature[attr.name()] = f[attr.name()]
                self.new_features.append(feature)

    def apply(self):
        self.output_layer = layer_helper.create_layer(os.path.splitext(os.path.basename(self.dlg.location()))[0], self.attributes, self.layer1)
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
