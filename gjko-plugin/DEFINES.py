from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry
from PyQt4.QtCore import *

"""
This file contains definition of fields, layers used accross this plugin.
"""

""" FEATURE FIELD """
FIELD_CODCAT = 'COD_CATAST'
FIELD_OBJECTID = 'OBJECTID'
FIELD_UUID = 'UUID'
FIELD_VOLUME_HEIGHT = 'UN_VOL_AV'
FIELD_VOLUME_AREA = 'AREA'
FIELD_SV = 'SV'
FIELD_NEIGHBORS_UUID = 'NEIGHBORS'

""" LAYER """
AYER_NEIGHBORS = 'Neighbors'

FIELD_CATID = 'ID_LR'
FIELD_AREA = 'AREA'
FIELD_PERIMETER = 'PERIMETER'
FIELD_HEIGHT = 'HEIGHT'
FIELD_COMPACT_RATIO = 'COMP_RATIO'

LAYER_MEM_FIELDS = [ 
        QgsField(FIELD_CATID, QVariant.String),
#        QgsField(FIELD_NEIGHBORS_UUID,  QVariant.String), 
        QgsField(FIELD_AREA,  QVariant.Double),
        QgsField(FIELD_PERIMETER,  QVariant.Double),
        QgsField(FIELD_HEIGHT,  QVariant.Double),
        QgsField(FIELD_COMPACT_RATIO,  QVariant.Double)]
