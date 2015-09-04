from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry
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

def compute_SVmultiple(features, neighbors):
    # I need to remove from the compute the abjacent points
    # I have multiple scenario like:
    #  - abajenct
    #  - completly on top of feature
    # hum ...
    # I need to compute the part of perimeter that it is in common

    total_wall = 0
    total_area = 0
    total_vol = 0
    geometries = []
    for uuid in neighbors:
        g = features[uuid].geometry()
        total_area += g.area()
        height = features[uuid][FIELD_VOLUME_HEIGHT]
        total_vol += g.area() * height
        total_wall += g.length() * height
        geometries.append(g)
    
    # Remove from length the common parts.
    for i in range(0, len(geometries)):
        g = geometries[i]
        for x in range(i, len(geometries)):
            neested = geometries[x]
            if not g.equals(neested) and not g.disjoint(neested):
                intersection = g.intersection(neested)
                h1 = features[neighbors[i]][FIELD_VOLUME_HEIGHT]
                h2 = features[neighbors[x]][FIELD_VOLUME_HEIGHT]
                if h1 < h2:
                    total_wall -= intersection.length() * h1
                else:
                    total_wall -= intersection.length() * h2
                print("Geometry 1 len: " + str(g.length()) + " geometry 2 len: " + str(neested.length()) + " intersection len: " + str(intersection.length()))
    return (total_area * 2 + total_wall) / total_vol



def compute_SVs(layer_neighbors, layer_vols):
   
    features = load_feature_dict_id(layer_neighbors)
    features_uuid = load_feature_dict_UUID(layer_vols)
    layer_neighbors.startEditing()
    try:
        for f in features.values():
            neighbors = f[FIELD_NEIGHBORS_UUID].split(',')
            SV = 0.0
            if len(neighbors) == 1:
                SV = compute_SV(features_uuid[neighbors[0]])
            else:
                SV = compute_SVmultiple(features_uuid, neighbors)
                show_features(layer_vols, features_uuid, neighbors)
            f[FIELD_SV] = SV
            layer_neighbors.updateFeature(f)
    except:
        layer_neighbors.rollBack()
        raise
    layer_neighbors.commitChanges()
