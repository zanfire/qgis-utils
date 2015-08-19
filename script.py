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

try:
    if popolateNeighbors:
        print("Populating neighbors")
        for f in features.values():
            neighbors = list_neighbors(index, features, f)
            print("For feautre " + f[FIELD_UUID] + " -> " + ",".join(neighbors))
            if len(neighbors) > 0: 
                f[FIELD_NEIGHBORS_UUID] = ','.join(neighbors)
            layer.updateFeature(f)
    layer.commitChanges()
    
    for f in features.values():
        neighbors = list_neighbors_of_neighbors(f, features_uuid)
        if len(neighbors) > 0:
            print("OLD " + f[FIELD_UUID] + " -> " + f[FIELD_NEIGHBORS_UUID])
            print("NEW " + f[FIELD_UUID] + " -> " + ",".join(neighbors))
            if f[FIELD_NEIGHBORS_UUID] !=  (",".join(neighbors)):
                selection = [f.id()]
                for x in neighbors:
                    selection.append(features_uuid[x].id())
                layer.setSelectedFeatures(selection)

    # Add the consolidate step.
    layer.commitChanges()
except:
    print("Failed script")
    layer.rollBack()
    raise
