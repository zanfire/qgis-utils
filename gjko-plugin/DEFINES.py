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
FIELD_CADASTRE_USAGE = 'USO'

FIELD_CATID                     = 'ID_LR'
FIELD_AREA                      = 'AREA'
FIELD_PERIMETER                 = 'PERIMETER'
FIELD_HEIGHT                    = 'HEIGHT'
FIELD_PERIMETER_ADJACENT        = 'PERIM_ABJ'
FIELD_CODISTAT                  = 'COD_ISTAT'

FIELD_SEZ_ISTAT                 = 'SEZ2011'
FIELD_CSV_SEZ_AGE               = 'SEZ_AGE'


# Final tables

FIELD_ID_CADASTRE = 'ID_CAD'
FIELD_ID_MEM      = 'ID_MEM' #9   identifier of the MEM building,  only buildings that presumably use heating and/or cooling
FIELD_USE         = 'USE' #3   residential (E1) or non-residential (En1) building      
FIELD_ID_EPC      = 'ID_EPC' #6   identifier of EPCs data     USE + codice catastale
FIELD_TYPOLOGY    = 'TYPOLOGY' #8   identifier of compactness-age typology (serve compact_r e age)  A1, A2,
FIELD_ID_ISTAT    = 'ID_ISTAT' #8   identifier of ISTAT zone
FIELD_ID_OMI      = 'ID_OMI' #6   identifier of OMI zone    
# = '' Energy fields   #    descrizione da dove note
FIELD_FOOT_AREA        = 'FOOT_AREA' #4   footprint building area area   
FIELD_FLOOR_AREA  = 'FLOOR_AREA' #10      (sommatoria un-vol_MEM)  
FIELD_VOL_GROSS   = 'VOL_GROSS' #6       (sommatoria un-vol_MEM)  
FIELD_DISP_SURF   = 'DISP_SURF' #9   dispersing surface  (sommatoria un-vol_MEM)  
FIELD_COMPACT_R   = 'COMPACT_R' #9   S/V (considera tutte le un-vol_MEM) 
FIELD_WALL_SURF   = 'WALL_SURF' #9   walls surface   (sommatoria un-vol_MEM)  
FIELD_AGE         = 'AGE' #3       ID_EPC o ID_ISTAT   da fare per ID_EPC
FIELD_WIND_R      = 'WIND_R' #6   window ratio (to dispersing surface)    ID_EPC o TYPOLOGY   wind_r da verificare per typology
FIELD_WIND_SURF   = 'WIND_SURF' #9   window surface  disp_surf*wind_r    
FIELD_U_ENV       = 'U_ENV' #5   Envelope U-value    ID_EPC o TYPOLOGY   
FIELD_U_ROOF      = 'U_ROOF' #6   Roof U-value    ID_EPC o TYPOLOGY   
FIELD_U_GROUND    = 'U_GROUND' #8   Ground U-value  ID_EPC o TYPOLOGY   
FIELD_U_WIND      = 'U_WIND' #6   Window U-value  ID_EPC o TYPOLOGY   
FIELD_EPH         = 'EPH' #3   Primary Energy Heating  ID_EPC o TYPOLOGY   
FIELD_ETH         = 'ETH' #3   Thermal Energy Heating  ID_EPC o TYPOLOGY   
FIELD_ETC         = 'ETC' #3   Thermal Energy Cooling  ID_EPC o TYPOLOGY   
FIELD_EFER        = 'EFER' #4   Energy from RES ID_EPC o TYPOLOGY   
FIELD_EPW         = 'EPW' #3   Primary Energy DHW  ID_EPC o TYPOLOGY   
FIELD_EPT         = 'EPT' #3   Primary Energy Total    ID_EPC o TYPOLOGY   
FIELD_E_HEAT      = 'E_HEAT' #6   overall efficiency of the heating system    ID_EPC o TYPOLOGY   
FIELD_E_DHW       = 'E_DHW' #5   overall efficiency of the dhw system    ID_EPC o TYPOLOGY   
FIELD_E_H_DHW     = 'E_H_DHW' #7   overall efficiency of the heating & dhw system  ID_EPC o TYPOLOGY   
FIELD_PV_AREA      = 'PV_AREA' #6   surface of photovoltaic panels  ID_EPC  if not available use 0.
FIELD_ST_AREA      = 'ST_AREA' #6   surface of solar thermal panels ID_EPC  if not avialable use 0. 

FIELD_AREA_GROSS = 'AREA_GROSS'
FIELD_VOL_GROSS = 'VOL_GROSS'
FIELD_WALL_SURF = 'WALL_SURF'
FIELD_DISP_SURF = 'DISP_SURF'
FIELD_AREA_R = 'AREA_R'
FIELD_AREA_NET = 'AREA_NET'
FIELD_VOL_R = 'VOL_R'
FIELD_VOL_NET = 'VOL_NET'
FIELD_H_LEVEL = 'H_LEVEL'
FIELD_N_LEVEL = 'N_LEVEL'
FIELD_FLOOR_AREA = 'FLOOR_AREA'

LAYER_BUILDING_FIELD = [ 
        QgsField(FIELD_ID_CADASTRE, QVariant.String),
        QgsField(FIELD_ID_MEM, QVariant.String),
        QgsField(FIELD_USE, QVariant.String),
        QgsField(FIELD_ID_EPC, QVariant.String),
        QgsField(FIELD_TYPOLOGY, QVariant.String),
        QgsField(FIELD_ID_ISTAT, QVariant.String),
        QgsField(FIELD_ID_OMI, QVariant.String),
        QgsField(FIELD_FOOT_AREA, QVariant.Double),
        QgsField(FIELD_FLOOR_AREA, QVariant.Double),
        QgsField(FIELD_VOL_GROSS, QVariant.Double),
        QgsField(FIELD_VOL_NET, QVariant.Double),
        QgsField(FIELD_DISP_SURF, QVariant.Double),
        QgsField(FIELD_COMPACT_R, QVariant.Double),
        QgsField(FIELD_WALL_SURF, QVariant.Double),
        QgsField(FIELD_AGE, QVariant.String),
        QgsField(FIELD_WIND_R, QVariant.Double),
        QgsField(FIELD_WIND_SURF, QVariant.Double),
        QgsField(FIELD_U_ENV, QVariant.Double),
        QgsField(FIELD_U_ROOF, QVariant.Double),
        QgsField(FIELD_U_GROUND, QVariant.Double),
        QgsField(FIELD_U_WIND, QVariant.Double),
        QgsField(FIELD_EPH, QVariant.Double),
        QgsField(FIELD_ETH, QVariant.Double),
        QgsField(FIELD_ETC, QVariant.Double),
        QgsField(FIELD_EFER, QVariant.Double),
        QgsField(FIELD_EPW, QVariant.Double),
        QgsField(FIELD_EPT, QVariant.Double),
        QgsField(FIELD_E_HEAT, QVariant.Double),
        QgsField(FIELD_E_DHW, QVariant.Double),
        QgsField(FIELD_E_H_DHW, QVariant.Double),
        QgsField(FIELD_PV_AREA, QVariant.Double),
        QgsField(FIELD_ST_AREA, QVariant.Double)
        ]

LAYER_VOLUMES_FIELDS = [
        QgsField(FIELD_ID_CADASTRE, QVariant.String),
        #un-vol_MEM  identifier of the MEM volumetric unit
        QgsField(FIELD_USE, QVariant.String), # residential (E1) or non-residential (En1) building
        QgsField(FIELD_ID_EPC, QVariant.String), # identifier of EPCs data
        #TYPOLOGY    identifier of compactness-age typology
        #ID_ISTAT    identifier of ISTAT zone
        #ID_OMI  identifier of OMI zone
        QgsField(FIELD_ID_MEM, QVariant.String),     # identifier of the MEM building belongs to 
#Energy Fields   descrizione
        QgsField(FIELD_HEIGHT, QVariant.Double),  # height of the volumetric unit
        QgsField(FIELD_AREA_GROSS, QVariant.Double),  # gross area
        QgsField(FIELD_VOL_GROSS, QVariant.Double),   # gross volume
        QgsField(FIELD_WALL_SURF, QVariant.Double),   # walls surface
        QgsField(FIELD_DISP_SURF, QVariant.Double),   # dispersing surface
        QgsField(FIELD_AREA_R, QVariant.Double),  # net area to gross area ratio
        QgsField(FIELD_AREA_NET, QVariant.Double),    # net area
        QgsField(FIELD_VOL_R, QVariant.Double),   # net volume to gross volume ratio
        QgsField(FIELD_VOL_NET, QVariant.Double), # net volume
        QgsField(FIELD_H_LEVEL, QVariant.Double), # # average level's height
        QgsField(FIELD_N_LEVEL, QVariant.Int), # # number of levels
        QgsField(FIELD_FLOOR_AREA, QVariant.Double)  # #net floor area
        ]
