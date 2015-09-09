# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from ..resources import *

class Action(object):
    def __init__(self, iface, menu_name, name):
        self.iface = iface
        self.menu = menu_name
        self.action = QAction(QIcon(":/plugins/Gjko/icon.png"), name, self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    def load(self):  
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(self.menu, self.action)

    def unload(self):
        self.iface.removePluginMenu(self.menu, self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self): 
        print("Default implementation.")

