# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

from Action import Action
from ..dialogs import AssignClassDialog
from ..util import layer_helper
from ..DEFINES import *
from ..logic import mem

class AssignClassAction(Action):
    def __init__(self, iface, menu_name):
        super(AssignClassAction, self).__init__(iface, menu_name, "Assign class...")

    def run(self): 
        self.dlg = AssignClassDialog() 
        self.dlg.show()
        result = self.dlg.exec_() 
        if result == 1:
            energy_layer = layer_helper.get_layer(self.dlg.energy_layer_name())
            cert_layer = layer_helper.get_layer(self.dlg.certificate_layer_name())
            istat_layer = layer_helper.get_layer(self.dlg.istat_layer_name())
            self.compute_epoch(energy_layer, cert_layer, istat_layer)
            print("Completed.")

    def initialize(self, name, baselayer):
        layer = layer_helper.get_layer(name)
        if layer != None:
            # Error or not?
            # Fill with needed attribute! 
            return layer
        # Check if exists layer name
        # Create layer.
        layer = layer_helper.create_layer(name, LAYER_MEM_INTERMEDIATE_FIELDS, baselayer)
        return layer

    def compute_epoch(self, energy_layer, cert_layer, istat_layer):
        istat_features = layer_helper.load_features(istat_layer)
        index = layer_helper.build_spatialindex(istat_features.values())
        # For each building I need to determine the epoch.
        #   - This step can performed looking in the certificate layer and use the landregister id for retrieving this information
        #   - If whe dont' have this information we procede with the spatial index from ISTAT layer nad get a supposed data.
        features = energy_layer.getFeatures()
        certificates = layer_helper.load_features_with_id(FIELD_CERT_CODCAT, cert_layer.getFeatures())
        for f in features:
            id_landregister = f[FIELD_CATID][:f[FIELD_CATID].rfind('_')]
            epoch = None
            if id_landregister in certificates.keys():
                epoch = certificates[id_landregister][FIELD_CERT_EPOCH]
            if epoch is None:
                # Search with ISTAT and spatial index
                ids = index.intersections(f.geometry())
                for i in ids:
                    epoch = istat_features[i][FIELD_ISTAT_EPOCH]
            if epoch is None:
                epoch = 'DEFAULT'

        print('Computed')
