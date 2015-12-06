# Specification input data

This is a specs document about how and what data are needed for this plugin.
This plugin is divided in three separated steps.

We describe needed data for each step. 

## Step 1 - Assign ID_CAD

This step need the follow layers:
 - Volumes layer
 - Cadastre layer
 - Cadastre terrains layer

This step generate a layer called SpatialJoin containing Volumes layer fields
 plus COD_CATAST.

This step is domain specific spatial join that assign for each volume in 
 volumes layer the right cadastre identification code.

### Volumes layer requirements


## Step 2 - Create energy layers

This step require the spatial join layer created in the previous step.

This step create two separate layer


