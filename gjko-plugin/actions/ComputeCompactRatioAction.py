# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

from Action import Action
from ..dialogs import ComputeCompactRatioDialog
from ..util import layer_helper
from ..DEFINES import *
from ..logic import mem

class ComputeCompactRatioAction(Action):
    def __init__(self, iface, menu_name):
        super(ComputeCompactRatioAction, self).__init__(iface, menu_name, "Compute compact ratio")

    def run(self): 
        dlg = ComputeCompactRatioDialog() 
        dlg.show()
        result = dlg.exec_() 
        if result == 1:
            layer = self.initialize(dlg.working_layer_name())
            # Get from interessed layer the selected features. Better if all is stored in one layer instead of on two distigushed layer.
            land_register_layer = layer_helper.get_layer(dlg.land_register_layer_name())
            volumes_layer = layer_helper.get_layer(dlg.volumes_layer_name())
            
            self.compute(layer, land_register_layer, volumes_layer)
        else:
            print("Cancel!")
        print("Completed.")

    def initialize(self, name):
        layer = layer_helper.get_layer(name)
        if layer != None:
            # Error or not?
            # Fill with needed attribute! 
            return layer
        # Check if exists layer name
        # Create layer.
        layer = layer_helper.create_layer(name, LAYER_MEM_FIELDS)
        return layer

    def compute(self, layer, land_register, volumes):
        QgsMessageLog.logMessage("Starting compation ...", "Gjko", QgsMessageLog.INFO)
        features = volumes.getFeatures()

        new_features = []
        for f in features:
            feature = QgsFeature(layer.pendingFields())
            feature.setGeometry(f.geometry())
            mem.compute_simple_compact_ratio(f, feature)
            new_features.append(feature)
        QgsMessageLog.logMessage("Adding " + str(len(new_features))+" new features.", "Gjko", QgsMessageLog.INFO)
        layer.startEditing()
        layer.dataProvider().addFeatures(new_features)
        layer.commitChanges()
