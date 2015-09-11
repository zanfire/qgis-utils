from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry, QgsVectorFileWriter, QgsSpatialIndex, QgsGeometry
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

def create_layer(name, attributes, baselayer = None, layertype = 'Polygon'):
    layerattr = ''
    if baselayer != None:
        layerattr = '?crs=' + baselayer.crs().authid()
        layerattr += '&index=yes'
    layer = QgsVectorLayer(layertype + layerattr, name, "memory") # memory
    pr = layer.dataProvider()
    layer.startEditing()
    pr.addAttributes(attributes)
    layer.updateFields()
    layer.commitChanges()
    QgsMapLayerRegistry.instance().addMapLayer(layer) 
    return layer

def save_layer(layer, name,location):
    error = QgsVectorFileWriter.writeAsVectorFormat(layer, os.path.join(location, name + ".shp"), "CP1250", None, "ESRI Shapefile")

def get_layer(name):
    layers = iface.legendInterface().layers()
    for layer in layers:
        if layer.name() == name:
            return layer
    return None

def load_features(layer):
    return {f.id(): f for f in layer.getFeatures()}

def load_features_with_id(id, layer):
    return {f[id]: f for f in layer.getFeatures()}

def build_spatialindex(features):
    index = QgsSpatialIndex()
    for f in features:
        index.insertFeature(f)
    return index

def copy_geometry(feature):
    return QgsGeometry(feature.geometry())
    #polygon = feature.geometry().asQPolygonF()
    #return QgsGeometry.fromQPolygonF(polygon)
 
# Move in UI helper

def show_features(layer, features):
    selection = []
    for x in features:
        selection.append(x.id())
    layer.setSelectedFeatures(selection)
    iface.actionZoomToSelected().trigger()

