from qgis.utils import iface
import logging

layer = iface.activeLayer()

layer.startEditing()

popolateNeighbors = False
features = load_feature_dict_id(layer)
if features[0].fields().indexFromName(FIELD_NEIGHBORS_UUID) == -1:
    layer.dataProvider().addAttributes([QgsField(FIELD_NEIGHBORS_UUID, QVariant.String)])
    print("Added field: " + FIELD_NEIGHBORS_UUID)
    popolateNeighbors = True
    layer.updateFields()
else:
    print("Field " + FIELD_NEIGHBORS_UUID + " is present")

# Reload 
features = load_feature_dict_id(layer)
features_uuid = load_feature_dict_UUID(layer)
index = build_spatialindex(features)

if popolateNeighbors:
    for f in features.values():
        neighbors = list_neighbors(index, features, f)
        print("For feautre " + f[FIELD_UUID] + " -> " + ",".join(neighbors))
        f[FIELD_NEIGHBORS_UUID] = ','.join(neighbors)
        layer.updateFeature(f)

# Add the consolidate step.
layer.commitChanges()

