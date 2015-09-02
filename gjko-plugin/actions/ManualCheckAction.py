# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *

from ..dialogs import ManualCheckDialog
from ..util import layer_helper
from Action import Action
from ..DEFINES import *

class ManualCheckAction(Action):
    def __init__(self, iface, menu_name):
        super(ManualCheckAction, self).__init__(iface, menu_name, "Manualy check selected features...")

    def run(self):
        dlg = ManualCheckDialog() 
        dlg.show()
        result = dlg.exec_() 
