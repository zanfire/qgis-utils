from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_SpatialJoinCadastre import Ui_Dialog

class SpatialJoinDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.volumesCombo.addItem(l.name())
            self.ui.cadastreCombo.addItem(l.name())
            self.ui.cadastreTerrainCombo.addItem(l.name())

    def working_layer_name(self):
        return self.ui.layerName.text()
    
    def volumes_layer_name(self):
        return str(self.ui.volumesCombo.currentText())

    def cadastre_layer_name(self):
        return str(self.ui.cadastreCombo.currentText())

    def cadastre_terrain_layer_name(self):
        return str(self.ui.cadastreTerrainCombo.currentText())

