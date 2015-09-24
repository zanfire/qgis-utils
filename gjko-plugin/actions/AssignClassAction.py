# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

from Action import Action
from ..dialogs import AssignClassDialog
from ..util import layer_helper, reader_csv
from ..DEFINES import *
from ..logic import mem, code_generator

class AssignClassAction(Action):
    def __init__(self, iface, menu_name):
        super(AssignClassAction, self).__init__(iface, menu_name, "Assign class...")
    
    def create_dialog(self):
        return AssignClassDialog() 


    def initialize(self):
        self.energy_layer = layer_helper.get_layer(self.dlg.energy_layer_name())
        self.istat_layer = layer_helper.get_layer(self.dlg.istat_layer_name())
        self.istat_csv = reader_csv.ISTAT(self.dlg.istat_csv_file())
        self.epcs_csv = reader_csv.EPCs(self.dlg.epcs_csv_file())

    def compute(self):
        istat_features = layer_helper.load_features(self.istat_layer)
        index = layer_helper.build_spatialindex(istat_features.values())

        self.energy_layer.startEditing()
        for f in self.energy_layer.getFeatures():
            ids = index.intersects(f.geometry().boundingBox())
            for i in ids:
                codistat = str(int(istat_features[i]['SEZ2011']))
                epoch = self.istat_csv.get(codistat)
                if epoch == None:
                    continue
                f[FIELD_EPOCH] = epoch
                f[FIELD_CLASS] = code_generator.get_code(f[FIELD_TYPE_USAGE], f[FIELD_EPOCH], f[FIELD_COMPACT_RATIO])
                f[FIELD_CODISTAT] = codistat
                #epcs = self.epcs_csv.get(f[FIELD_TYPE_USAGE] + '.' + f[FIELD_CODCAT])
                epcs = self.epcs_csv.get(reader_csv.codcat_to_epcs(f[FIELD_TYPE_USAGE], f[FIELD_CODCAT]))
                if epcs != None:
                    # Fill data.
                    f[FIELD_EPCs_AVAILABLE] = 1
                self.energy_layer.updateFeature(f)
        self.energy_layer.commitChanges()

