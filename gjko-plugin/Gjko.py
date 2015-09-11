# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from actions import *
from resources import *

class Gjko: 

    def __init__(self, iface):
        menuName = "&Energy efficency for building"
        self.menu = QMenu(iface.mainWindow())
        self.menu.setObjectName("gjkoMenu")
        self.menu.setTitle(menuName)

        # Save reference to the QGIS interface
        self.iface = iface
        self.actions = []
        self.actions.append(ComputeCompactRatioAction(iface, menuName))
        self.actions.append(AssignClassAction(iface, menuName))
        self.actions.append(ManualCheckAction(iface, menuName))

    def initGui(self): 
        #menuBar = self.iface.mainWindow().menuBar()
        #menuBar.insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.menu)

        for a in self.actions:
            a.load()
            self.menu.addAction(a.action)

    def unload(self):
         for a in self.actions:
            a.unload()
         #self.menu.deleteLater()
