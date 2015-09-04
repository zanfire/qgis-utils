from qgis.utils import iface
from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import DEFINES
import layer_helper

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

def show_features(layer, features, neighbors):
    selection = []
    for x in neighbors:
        selection.append(features[x].id())
    layer.setSelectedFeatures(selection)
    box = layer.boundingBoxOfSelected()
    iface.mapCanvas().setExtent(box)
    iface.mapCanvas().refresh()

def compute_SVs():
    layer_neighbors = get_layer(LAYER_NEIGHBORS)
    layer_vols = get_layer(LAYER_VOLUMES)
    
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
