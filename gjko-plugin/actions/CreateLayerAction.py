# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

from ..dialogs import CreateLayerDialog
#import ..layer_helper

from Action import Action

class CreateLayerAction(Action):
    def __init__(self, iface, menu_name):
        super(CreateLayerAction, self).__init__(iface, menu_name, "Create working Layer")

    def run(self):
        dlg = CreateLayerDialog() 
        dlg.show()
        result = dlg.exec_() 
        # See if OK was pressed
        if result == 1:    
            #layer = layer_helper.get_layer(DEFINES.LAYER_NEIGHBORS)
            if layer != None:
                QMessageBox.error(None, 'Message', 'Continue?\n (seeing feature ' + str(idx)+ ')')
                return

            #layer = layer_helper.create_layer(DEFINES.LAYER_NEIGHBORS, DEFINES.LAYER_NEIGHBORS_FIELDS)
            print("Completed.")
