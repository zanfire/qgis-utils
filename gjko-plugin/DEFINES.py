from qgis.core import QgsVectorLayer, QgsField, QgsMapLayerRegistry
from PyQt4.QtCore import *

"""
This file contains definition of fields, layers used accross this plugin.
"""

""" FEATURE FIELD """
FIELD_CODCAT = 'COD_CATAST'
FIELD_VOLUME_HEIGHT = 'UN_VOL_AV'
FIELD_CERT_CODCAT = 'UN_VOL_AV'
FIELD_CERT_EPOCH = 'UN_VOL_AV'
FIELD_ISTAT_EPOCH = 'UN_VOL_AV'
FIELD_CADASTRE_TERRAIN_ID = 'CHIAVE'

FIELD_CATID                     = 'ID_LR'
FIELD_AREA                      = 'AREA'
FIELD_PERIMETER                 = 'PERIMETER'
FIELD_HEIGHT                    = 'HEIGHT'
FIELD_PERIMETER_ADJACENT        = 'PERIM_ABJ'
FIELD_DISPERSING_SURFACE        = 'DISP_SURF'
FIELD_COMPACT_RATIO             = 'COMP_RATIO'
FIELD_EPOCH                     = 'EPOCH'
FIELD_CLASS                     = 'CLASS'
#FIELD_CODCAT                    = 'COD_CAD'
FIELD_CODISTAT                  = 'COD_ISTAT'
FIELD_EPCs_AVAILABLE            = 'EPCS_AVAI'

LAYER_MEM_INTERMEDIATE_FIELDS = [ 
        QgsField(FIELD_CATID, QVariant.String),
        QgsField(FIELD_AREA,  QVariant.Double),
        QgsField(FIELD_PERIMETER,  QVariant.Double),
        QgsField(FIELD_PERIMETER_ADJACENT,  QVariant.Double),
        QgsField(FIELD_HEIGHT,  QVariant.Double),
        QgsField(FIELD_DISPERSING_SURFACE,  QVariant.Double),
        QgsField(FIELD_COMPACT_RATIO,  QVariant.Double)]

LAYER_MEM_FINAL_FIELDS = [ 
        QgsField(FIELD_CATID, QVariant.String),
        QgsField(FIELD_COMPACT_RATIO,  QVariant.Double),
        QgsField(FIELD_EPOCH, QVariant.String),
        QgsField(FIELD_CLASS, QVariant.String),
        QgsField(FIELD_CODISTAT, QVariant.String),
        QgsField(FIELD_CODCAT, QVariant.String),
        QgsField(FIELD_EPCs_AVAILABLE, QVariant.Int)]
