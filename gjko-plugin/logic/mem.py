from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry, QgsGeometry
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ..DEFINES import *
from ..util import layer_helper


def build_neighbors():
    layer_max_ext = layer_helper.get_layer(DEFINES.LAYER_MAX_EXTENSION)
    layer_vols = layer_helper.get_layer(DEFINES.LAYER_VOLUMES)
    layer_neighbors = layer_helper.get_layer(DEFINES.LAYER_NEIGHBORS)

    features_max_exts = helper.load_features(layer_max_ext)
    features_vols = helper.load_features(layer_vols)
    
    index = helper.build_spatialindex(features_vols)
    new_features = []
    for f in features_max_exts.values(): 
        ids = index.intersects(f.geometry().boundingBox())
        neighbors = []
        fet = QgsFeature()
        fet.setGeometry(f.geometry())
        for i in ids:
            if f.geometry().contains(features_vols[i].geometry()):
                neighbors.append(features_vols[i][FIELD_UUID])
        fet.setAttributes([ neighbors[0], ','.join(neighbors), 0.0])
        new_features.append(fet)
    layer_neighbors.startEditing()
    layer_neighbors.dataProvider().addFeatures(new_features)
    layer_neighbors.commitChanges()

def get_intersection(g1, g2):
    result = []
    r1 = QgsGeometry.fromPolyline(g1.asPolygon()[0])
    r2 = QgsGeometry.fromPolyline(g2.asPolygon()[0])
    if not r1.equals(r2) and r1.intersects(r2):
        i = r1.intersection(r2)
        result.append(QgsGeometry(i))
    return result
  
def dispersing_surface(index, feature, features):
    fg = feature.geometry()
    ids = index.intersects(fg.boundingBox())
    touch = 0
    perimeter_adjacent = 0
    for i in ids:
        f = features[i]
        g = f.geometry()
        if (f != feature and not feature.geometry().disjoint(f.geometry())):
            intersection_set = get_intersection(g, fg)
            h = f[FIELD_VOLUME_HEIGHT]
            h2 = feature[FIELD_HEIGHT]
            if h2 <= h:
                h = h2
            for intersection in intersection_set:
                perimeter_adjacent += intersection.length()
                touch += intersection.length() * h
    feature[FIELD_PERIMETER_ADJACENT] = perimeter_adjacent
    feature[FIELD_DISPERSING_SURFACE] = feature[FIELD_AREA] * 2 + (feature[FIELD_PERIMETER] * feature[FIELD_HEIGHT]) - touch

"""
Compute compact ratio only on a simple volume without adiacent volumes. 
"""
def compute_simple_compact_ratio(inFeature, outFeature):
    # Compute S / V.
    geom = inFeature.geometry()
    base_area = geom.area()
    perimeter = geom.length()
    height = inFeature[FIELD_VOLUME_HEIGHT]
    S = base_area * 2 + perimeter * height 
    V = base_area * height
    SV = S / V
    outFeature[FIELD_CATID] = inFeature[FIELD_CODCAT]
    outFeature[FIELD_AREA] = base_area
    outFeature[FIELD_HEIGHT] = height
    outFeature[FIELD_PERIMETER] = perimeter
    outFeature[FIELD_COMPACT_RATIO] = SV

def compute_multiple_compact_ratio(features):
    total_vol = 0
    total_disp = 0
    for f in features:
        total_vol += f[FIELD_HEIGHT] * f[FIELD_AREA]
        total_disp += f[FIELD_DISPERSING_SURFACE]
    mcr = total_disp / total_vol
    for f in features:
        f[FIELD_MULTIPLE_COMPACT_RATIO] = mcr

