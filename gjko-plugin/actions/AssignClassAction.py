# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
import math

from Action import Action
from ..dialogs import AssignClassDialog
from ..util import layer_helper, reader_csv
from ..DEFINES import *
from ..logic import mem, code_generator

class AssignClassAction(Action):
    def __init__(self, iface, menu_name):
        super(AssignClassAction, self).__init__(iface, menu_name, "3 - Assign EPC and Typology")
    
    def create_dialog(self):
        return AssignClassDialog() 


    def initialize(self):
        self.volumes_layer = layer_helper.get_layer(self.dlg.volumes_layer_name())
        self.building_layer = layer_helper.get_layer(self.dlg.building_layer_name())
        self.istat_layer = layer_helper.get_layer(self.dlg.istat_layer_name())
        self.istat_csv = reader_csv.ISTAT(self.dlg.istat_csv_file())
        self.epcs_csv = reader_csv.EPCs(self.dlg.epcs_csv_file())
        self.typology_csv = reader_csv.EPCs(self.dlg.typology_csv_file())

    def compute(self, progress):
        self.compute_volumes(progress)
        self.compute_building(progress)

    def compute_building(self, progress):
        QgsMessageLog.logMessage("Starting compute building ...")
        istat_features = layer_helper.load_features(self.istat_layer)
        building_features = layer_helper.load_features(self.building_layer)
        index = layer_helper.build_spatialindex(istat_features.values())

        self.updated_building_features = []
        count = 0
        count_max = len(building_features.values())
        for f in building_features.values():
            progress.emit(50 + int(count * (50.0 / count_max)))  
            count += 1
            ids = index.intersects(f.geometry().boundingBox())
            # guess the ISTAT code that have biggest area in this feature. 
            id_max = -1
            area_max = -1
            for i in ids:
                common = QgsGeometry(f.geometry().intersection(istat_features[i].geometry()))
                if common.area() > area_max:
                    id_max = i
                    area_max = common.area()
            if id_max > -1:
                codistat = str(int(istat_features[id_max][FIELD_SEZ_ISTAT]))
                f[FIELD_ID_ISTAT] = codistat
                f[FIELD_AGE] = self.istat_csv.get_element(codistat, FIELD_CSV_SEZ_AGE)
                f[FIELD_TYPOLOGY] = code_generator.get_code(f[FIELD_USE], f[FIELD_AGE], f[FIELD_COMPACT_R])
                id_mem = f[FIELD_ID_MEM]
                if id_mem in self.idmem_to_volumes.keys():
                    for vol in self.idmem_to_volumes[id_mem]:
                        vol[FIELD_TYPOLOGY] = f[FIELD_TYPOLOGY]
                        self.assign_volumes_values(vol, self.typology_csv, f[FIELD_TYPOLOGY])
                else:
                    QgsMessageLog.logMessage("id_mem missing ... " + id_mem)

                id_epc = reader_csv.codcat_to_epcs(f[FIELD_USE], f[FIELD_ID_CADASTRE])
                epcs = self.epcs_csv.get(id_epc)
                if epcs == None:
                    self.assign_building_values(f, self.typology_csv, f[FIELD_TYPOLOGY])
                if epcs != None:
                    f[FIELD_ID_EPC] = id_epc
                    epc_age = self.epcs_csv.get_element(id_epc, 'age')
                    if epc_age != None and epc_age != '' and epc_age != f[FIELD_AGE]:
                        f[FIELD_AGE] = epc_age
                        f[FIELD_TYPOLOGY] = code_generator.get_code(f[FIELD_USE], f[FIELD_AGE], f[FIELD_COMPACT_R])
                    
                    self.assign_building_values(f, self.epcs_csv, id_epc)
                    
                f[FIELD_FLOOR_AREA] = 0
                f[FIELD_VOL_NET] = 0
                for vol in self.idmem_to_volumes[f[FIELD_ID_MEM]]:
                    try:
                        f[FIELD_FLOOR_AREA] += vol[FIELD_FLOOR_AREA]
                        f[FIELD_VOL_NET] += vol[FIELD_VOL_NET]
                    except:
                        QgsMessageLog.logMessage("Same id_mem but different epc (different USO???)")
                self.updated_building_features.append(f)

    def compute_volumes(self, progress):
        volumes_features = layer_helper.load_features(self.volumes_layer)

        self.idmem_to_volumes = {}
        self.updated_volumes_features = []
        count = 0
        count_max = len(volumes_features.values())
        for f in volumes_features.values():
            progress.emit(int(count * (50.0 / count_max)))  
            count += 1
            id_epc = reader_csv.codcat_to_epcs(f[FIELD_USE], f[FIELD_ID_CADASTRE])
            epcs = self.epcs_csv.get(id_epc)
            if epcs != None:
                f[FIELD_ID_EPC] = id_epc
                self.assign_volumes_values(f, self.epcs_csv, id_epc)
            self.updated_volumes_features.append(f)
            # Update map with all features not only with EP# Update map with all features not only with EPCC
            id_mem = f[FIELD_ID_MEM]
            if id_mem in self.idmem_to_volumes.keys():
                self.idmem_to_volumes[id_mem].append(f)
            else:
                self.idmem_to_volumes[id_mem] = [ f ] 

    def apply(self):
        self.building_layer.startEditing()
        for f in self.updated_building_features:
            self.building_layer.updateFeature(f)
        self.building_layer.commitChanges()
        self.volumes_layer.startEditing()
        for f in self.updated_volumes_features:
            self.volumes_layer.updateFeature(f)
        self.volumes_layer.commitChanges()
        
        return None
    
    def assign_volumes_values(self, f, csv, id_elem):
        try:
            f[FIELD_AREA_R] = csv.get_element(id_elem, 'area_r')
            f[FIELD_VOL_R] = csv.get_element(id_elem, 'vol_r')
            f[FIELD_H_LEVEL] = csv.get_element(id_elem, 'h_level')
            f[FIELD_AREA_NET] = float(f[FIELD_AREA_GROSS]) * float(f[FIELD_AREA_R])
            f[FIELD_VOL_NET] = float(f[FIELD_VOL_GROSS]) * float(f[FIELD_VOL_R])
            n_level = float(f[FIELD_HEIGHT]) / float(f[FIELD_H_LEVEL])
            if math.modf(n_level) > 0.8:
                n_level = math.ceil(n_level)
            else:
                n_level = math.floor(n_level)
            if n_level < 1:
                n_level = 1
            f[FIELD_N_LEVEL] = n_level
            f[FIELD_FLOOR_AREA] = float(f[FIELD_AREA_NET]) * float(f[FIELD_N_LEVEL])
        except:
            QgsMessageLog.logMessage("Error for " + id_elem + " no values.")


    def assign_building_values(self, f, csv, id_elem):
        f[FIELD_WIND_R] = csv.get_element(id_elem, 'wind_r')
        f[FIELD_WIND_SURF] = csv.get_element(id_elem, 'wind_surf')
        f[FIELD_U_ENV] = csv.get_element(id_elem, 'u_env')
        f[FIELD_U_ROOF] = self.epcs_csv.get_element(id_elem, 'u_roof')
        f[FIELD_U_GROUND] = self.epcs_csv.get_element(id_elem, 'u_ground')
        f[FIELD_U_WIND] = csv.get_element(id_elem, 'u_wind')
        f[FIELD_EPH] = csv.get_element(id_elem, 'eph')
        f[FIELD_ETH] = csv.get_element(id_elem, 'eth')
        f[FIELD_ETC] = csv.get_element(id_elem, 'etc')
        f[FIELD_EFER] = csv.get_element(id_elem, 'efer')
        f[FIELD_EPW] = csv.get_element(id_elem, 'epw')
        f[FIELD_EPT] = csv.get_element(id_elem, 'ept')
        f[FIELD_E_HEAT] = csv.get_element(id_elem, 'e_heat')
        f[FIELD_E_DHW] = csv.get_element(id_elem, 'e_dhw')
        f[FIELD_E_H_DHW] = csv.get_element(id_elem, 'e_h_dhw')
        f[FIELD_PV_AREA] = csv.get_element(id_elem, 'fv_area', 0)
        f[FIELD_ST_AREA] = csv.get_element(id_elem, 'st_area', 0)
 
