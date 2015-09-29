from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_SpatialJoinCadastre import Ui_Dialog
import os

class SpatialJoinDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.layerName.setText(os.path.join(os.getenv('HOME'), "SpatialJoin.shp"))
        QtCore.QObject.connect(self.ui.locationButton, QtCore.SIGNAL('clicked()'), self.save_location_dialog)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.volumesCombo.addItem(l.name())
            self.ui.cadastreCombo.addItem(l.name())
            self.ui.cadastreTerrainCombo.addItem(l.name())

    def save_location_dialog(self):
        location = QtGui.QFileDialog.getSaveFileName(None, 'Shapefile file:', self.ui.layerName.text(), 'Shp (*.shp);; All files (*)')
        if len(location) > 0:
            self.ui.layerName.setText(location)
    
    def location(self):
        return self.ui.layerName.text()
    
    def volumes_layer_name(self):
        return str(self.ui.volumesCombo.currentText())

    def cadastre_layer_name(self):
        return str(self.ui.cadastreCombo.currentText())

    def cadastre_terrain_layer_name(self):
        return str(self.ui.cadastreTerrainCombo.currentText())

