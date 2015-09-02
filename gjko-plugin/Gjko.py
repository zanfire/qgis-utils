# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from actions import *

class Gjko: 

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.actions = []
        self.actions.append(ComputeCompactRatioAction(iface, "&Thesis"))
        self.actions.append(CreateLayerAction(iface, "&Thesis"))
        #self.actions.append(ComputeCompactRatioAction(iface, "&Thesis"))

    def initGui(self):
        for a in self.actions:
            a.load()

    def unload(self):
         for a in self.actions:
            a.unload()
