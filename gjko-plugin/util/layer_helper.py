from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry, QgsVectorFileWriter, QgsSpatialIndex, QgsGeometry
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

def create_layer(name, attributes, baselayer = None):
    layerattr = ''
    if baselayer != None:
        layerattr = '?crs=' + baselayer.crs().authid()
        layerattr += '&index=yes'
    layer = QgsVectorLayer("Polygon" + layerattr, name, "memory")
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

def build_spatialindex(features):
    index = QgsSpatialIndex()
    for f in features:
        index.insertFeature(f)
    return index

def copy_geometry(feature):
    polygon = feature.geometry().asQPolygonF()
    return QgsGeometry.fromQPolygonF(polygon)
 
# Move in UI helper

def show_neighbors(skip):
    layer_neighbors = get_layer(LAYER_NEIGHBORS)
    layer_vols = get_layer(LAYER_VOLUMES)
    features = load_feature_dict_id(layer_neighbors)
    features_uuid = load_feature_dict_UUID(layer_vols)
    
    idx = 0
    for f in features.values():
        # Skip first elements.
        if idx < skip:
            idx += 1
            continue

        neighbors = f[FIELD_NEIGHBORS_UUID].split(',')
        selection = []
        for x in neighbors:
            selection.append(features_uuid[x].id())
            layer_vols.setSelectedFeatures(selection)
        box = layer_vols.boundingBoxOfSelected()
        iface.mapCanvas().setExtent(box)
        iface.mapCanvas().refresh()
        reply = QMessageBox.question(None, 'Message', 'Continue?\n (seeing feature ' + str(idx)+ ')', QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.No:
            break
        idx += 1

def show_features(layer, features):
    selection = []
    for x in features:
        selection.append(x.id())
    layer.setSelectedFeatures(selection)
    iface.actionZoomToSelected().trigger()

