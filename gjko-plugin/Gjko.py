# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from actions import *
from resources import *

class Gjko: 

    menu = None
    tool_menu = None
    actions = []
    tool_actions = []

    def __init__(self, iface):
        menuName = "&Municipal Energy Model"
        self.menu = QMenu(iface.mainWindow())
        self.menu.setObjectName("gjkoMenu")
        self.menu.setTitle(menuName)
        menuToolName = "&Municipal Energy Model - tools"
        self.tool_menu = QMenu(iface.mainWindow())
        self.tool_menu.setObjectName("gjkoToolMenu")
        self.tool_menu.setTitle(menuToolName)


        # Save reference to the QGIS interface
        self.iface = iface
        self.actions.append(SpatialJoinAction(iface, menuName))
        self.actions.append(ComputeCompactRatioAction(iface, menuName))
        self.actions.append(AssignClassAction(iface, menuName))
        self.tool_actions.append(ManualCheckAction(iface, menuToolName))
        self.tool_actions.append(SpatialJoinMaxAreaAction(iface, menuToolName))

    def initGui(self): 
        for a in self.actions:
            a.load()
            self.menu.addAction(a.action)
        for a in self.tool_actions:
            a.load()
            self.tool_menu.addAction(a.action)
    
    def unload(self):
         for a in self.actions:
            a.unload()
         for a in self.tool_actions:
            a.unload()
