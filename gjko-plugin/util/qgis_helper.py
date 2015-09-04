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
