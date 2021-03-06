from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry, QgsVectorFileWriter, QgsSpatialIndex, QgsGeometry, QgsMessageLog
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import os

def create_layer(name, attributes, baselayer = None, layertype = 'Polygon', addregistry = True):
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
    if addregistry:
        QgsMapLayerRegistry.instance().addMapLayer(layer) 
    return layer

def save_layer(layer, location):
    error = QgsVectorFileWriter.writeAsVectorFormat(layer, location, "CP1250", layer.dataProvider().crs(), "ESRI Shapefile")
    #error = QgsVectorFileWriter.writeAsShapefile(layer, location, "CP1250")
    return error

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


def get_intersection_max_area(index, f, features):
    g = f.geometry()
    ids = index.intersects(g.boundingBox())
    #QgsMessageLog.logMessage("Intersection returns " + str(len(ids)) + " IDs.")
    if len(ids) == 1:
        if not g.disjoint(features[ids[0]].geometry()):
            return ids[0]
    elif len(ids) > 1:
        id_max = -1
        area_max = -1
        for i in ids:
            if not g.disjoint(features[i].geometry()):
                common = QgsGeometry(g.intersection(features[i].geometry()))
                if common.area() > area_max:
                    id_max = i
                    area_max = common.area()
        if id_max > -1:
            return id_max
    return -1
