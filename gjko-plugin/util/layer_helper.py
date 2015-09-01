from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def create_layer(name, attributes):
    layer = QgsVectorLayer("Polygon", name, "memory")
    pr = layer.dataProvider()
    layer.startEditing()
    pr.addAttributes(attributes)
    layer.updateFields()
    layer.commitChanges()
    QgsMapLayerRegistry.instance().addMapLayer(layer) 
    return layer

def get_layer(name):
    layers = iface.legendInterface().layers()
    for layer in layers:
        if layer.name() == name:
            return layer
    return None


def load_features(layer):
    return {f.id(): f for f in layer.getFeatures()}

def load_features_UUID(layer):
    return {f[FIELD_UUID]: f for f in layer.getFeatures()}

def build_spatialindex(features):
    index = QgsSpatialIndex()
    for f in features.values():
        index.insertFeature(f)
    return index


