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
            #volumes_layer = layer_helper.get_layer(self.dlg.volumes_layer_name())
            #layer = self.initialize(self.dlg.working_layer_name(), volumes_layer)
            #self.compute(layer, volumes_layer)
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

    def compute(self, layer, volumes):
        print('Computed')
