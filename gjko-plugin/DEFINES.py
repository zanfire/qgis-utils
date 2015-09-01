from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry
from PyQt4.QtCore import *

"""
This file contains definition of fields, layers used accross this plugin.
"""

""" FEATURE FIELD """
FIELD_OBJECTID = 'OBJECTID'
FIELD_UUID = 'UUID'
FIELD_VOLUME_HEIGHT = 'UN_VOL_AV'
FIELD_VOLUME_AREA = 'AREA'
FIELD_SV = 'SV'
FIELD_NEIGHBORS_UUID = 'NEIGHBORS'

""" LAYER """
LAYER_MAX_EXTENSION = 'Estratto_MassimaEstensione'
LAYER_VOLUMES = 'Estratto_UnitaVolumetrica-Pulizia'
LAYER_NEIGHBORS = 'Neighbors'


LAYER_NEIGHBORS_FIELDS = [ QgsField(FIELD_UUID, QVariant.String),QgsField(FIELD_NEIGHBORS_UUID,  QVariant.String), QgsField(FIELD_SV,  QVariant.Double)]
