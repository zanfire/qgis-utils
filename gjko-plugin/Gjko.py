# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from actions import *
from resources import *

class Gjko: 

    def __init__(self, iface):
        menuName = "&Thesis"
        # Save reference to the QGIS interface
        self.iface = iface
        self.actions = []
        self.actions.append(ComputeCompactRatioAction(iface, menuName))
        #self.actions.append(CreateLayerAction(iface, menuName))
        self.actions.append(ManualCheckAction(iface, menuName))
        #self.actions.append(ComputeCompactRatioAction(iface, "&Thesis"))

    def initGui(self):
        for a in self.actions:
            a.load()

    def unload(self):
         for a in self.actions:
            a.unload()
