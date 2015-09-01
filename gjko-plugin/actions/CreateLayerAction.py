# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

from ..dialogs import CreateLayerDialog
from ..util import layer_helper
from Action import Action
from ..DEFINES import *

class CreateLayerAction(Action):
    def __init__(self, iface, menu_name):
        super(CreateLayerAction, self).__init__(iface, menu_name, "Create working Layer")

    def run(self):
        dlg = CreateLayerDialog() 
        dlg.show()
        result = dlg.exec_() 
        # See if OK was pressed
        if result == 1:    
            name = dlg.name()
            if len(name) == 0:
                QMessageBox.critical(None, 'Error', 'Layer name is missing, abort operation.')
                return
            location = dlg.location()
            if len(location) == 0:
                QMessageBox.critical(None, 'Error', 'Save folder is missing, abort operation.')
                return

            layer = layer_helper.get_layer(name)
            if layer != None:
                QMessageBox.critical(None, 'Error', 'Layer exists, abort operation.')
                return

            layer = layer_helper.create_layer(name, LAYER_NEIGHBORS_FIELDS)
            if layer != None:
                layer_helper.save_layer(layer, name, location)
            print("Completed.")
