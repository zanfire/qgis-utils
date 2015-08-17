from qgis.utils import iface
from PyQt4.QtCore import QVariant
import logging

FIELD_OBJECTID = 'OBJECTID'
FIELD_UUID = 'UUID'
FIELD_VOLUME_HEIGHT = 'UN_VOL_AV'
FIELD_VOLUME_AREA = 'AREA'
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
    print("Working on feature " + str(feature.id()) + " UUID " + feature[FIELD_UUID])
    # Compute S / V.
    geom = feature.geometry()
    base_area = geom.area()
    perimeter = geom.length()
    height = feature[FIELD_VOLUME_HEIGHT]
    print("Compute S/V: area " + str(base_area) + ", perimeter " + str(perimeter) + " height " + str(height))
    S = base_area * 2 + perimeter * height
    V = base_area * height
    SV = S / V
    print("Compute S/V: " + str(S) + " / " + str(V) + " = " + str(SV))
    return S / V

def compute_SVmultiple(feature, neighbors):
    # I need to remove from the compute the abjacent points
    # I have multiple scenario like:
    #  - abajenct
    #  - completly on top of feature
    # hum ...
    # I need to compute the part of perimeter that it is in common
    print("Working on feature " + str(feature.id()) + " UUID " + feature[FIELD_UUID])
    print("area " + str(feature["AREA"]))
    # Compute S / V.
    geom = feature.geometry()
    base_area = geom.area()
    perimeter = geom.length()
    height = feature[FIELD_VOLUME_HEIGHT]
    print("Compute S/V: area " + str(base_area) + ", perimeter " + str(perimeter) + " height " + str(height))
    S = base_area * 2 + perimeter * height
    V = base_area * height
    SV = S / V
    print("Compute S/V: " + str(S) + " / " + str(V) + " = " + str(SV))
    return S / V



def list_neighbors(index, features, feature):
    geom = feature.geometry()
    intersecting_ids = index.intersects(geom.boundingBox())
    # Initalize neighbors list and sum
    neighbors = []
    for intersecting_id in intersecting_ids:
        intersecting_f = features[intersecting_id]
        if (f != intersecting_f and not intersecting_f.geometry().disjoint(geom)):
            neighbors.append(intersecting_f[FIELD_UUID])
    return neighbors

def list_neighbors_of_neighbors(feature, features):
    # Add to the current feature
    neighbors_uuid = feature[FIELD_NEIGHBORS_UUID].split(',')
    for uuid in neighbors_uuid:
        # get neighbors
        neighbors_neighbors_uuid = features[uuid][FIELD_NEIGHBORS_UUID]
        for nested_uuid in neighbors_neighbors_uuid:
            if not nested_uuid in neighbors_uuid:
                list_neighbors_of_neighbors(features[uuid], features)

