# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

from Action import Action
from ..dialogs import ComputeCompactRatioDialog

class ComputeCompactRatioAction(Action):
    def __init__(self, iface, menu_name):
        super(ComputeCompactRatioAction, self).__init__(iface, menu_name, "Compute compact ratio")

    def run(self): 
        dlg = ComputeCompactRatioDialog() 
        dlg.show()
        result = dlg.exec_() 
        # See if OK was pressed
        if result == 1:    
            # Get from interessed layer the selected features. Better if all is stored in one layer instead of on two distigushed layer.

            print("Ok!")
        else:
            print("Cancel!")
        print("Completed.")
