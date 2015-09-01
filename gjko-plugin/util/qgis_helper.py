from qgis.utils import iface
from PyQt4.QtCore import QVariant
from PyQt4.QtCore import QPyNullVariant

import logging

FIELD_OBJECTID = 'OBJECTID'
FIELD_UUID = 'UUID'
FIELD_VOLUME_HEIGHT = 'UN_VOL_AV'
FIELD_VOLUME_AREA = 'AREA'
FIELD_SV = 'SV'
FIELD_NEIGHBORS_UUID = 'NEIGHBORS'

def load_feature_dict_id(layer):
    return {f.id(): f for f in layer.getFeatures()}

def load_feature_dict_UUID(layer):
    return {f[FIELD_UUID]: f for f in layer.getFeatures()}

def build_spatialindex(features):
    index = QgsSpatialIndex()
    for f in features.values():
        index.insertFeature(f)
    return index

def compute_SV(feature):
    #print("Working on feature " + str(feature.id()) + " UUID " + feature[FIELD_UUID])
    # Compute S / V.
    geom = feature.geometry()
    base_area = geom.area()
    perimeter = geom.length()
    height = feature[FIELD_VOLUME_HEIGHT]
    #print("Compute S/V: area " + str(base_area) + ", perimeter " + str(perimeter) + " height " + str(height))
    S = base_area * 2 + perimeter * height 
    V = base_area * height
    SV = S / V
    #print("Compute S/V: " + str(S) + " / " + str(V) + " = " + str(SV))
    return S / V

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

def list_neighbors(index, features, feature):
    geom = feature.geometry()
    intersecting_ids = index.intersects(geom.boundingBox())
    # Initalize neighbors list and sum
    neighbors = [feature[FIELD_UUID]]
    for intersecting_id in intersecting_ids:
        intersecting_f = features[intersecting_id]
        if (f != intersecting_f and not intersecting_f.geometry().disjoint(geom)):
            neighbors.append(intersecting_f[FIELD_UUID])
    return neighbors


def list_neighbors_of_neighbors(feature, features):
    # Add to the current feature
    if type(feature[FIELD_NEIGHBORS_UUID]) is QPyNullVariant:
        return []
    neighbors_uuid = feature[FIELD_NEIGHBORS_UUID].split(',')
    for uuid in neighbors_uuid:
        if type(features[uuid][FIELD_NEIGHBORS_UUID]) is QPyNullVariant:
            break
        neighbors_neighbors_uuid = features[uuid][FIELD_NEIGHBORS_UUID].split(',')
        for nested_uuid in neighbors_neighbors_uuid:
            if not nested_uuid in neighbors_uuid and not nested_uuid == feature[FIELD_UUID]: 
                print("Nested UUID " + nested_uuid + " not in " + ','.join(neighbors_uuid) + " ... adding")
                neighbors_uuid.append(nested_uuid)
                #list_neighbors_of_neighbors(features[uuid], features)
    return neighbors_uuid
