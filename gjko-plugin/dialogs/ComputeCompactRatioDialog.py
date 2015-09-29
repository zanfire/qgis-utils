from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_ComputeCompactRatio import Ui_Dialog
import os

class ComputeCompactRatioDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.volumesLayerPath.setText(os.path.join(os.getenv('HOME'), "Volumes.shp"))
        self.ui.buildingLayerPath.setText(os.path.join(os.getenv('HOME'), "Building.shp"))
        QtCore.QObject.connect(self.ui.locationButton1, QtCore.SIGNAL('clicked()'), self.save_location_dialog1)
        QtCore.QObject.connect(self.ui.locationButton2, QtCore.SIGNAL('clicked()'), self.save_location_dialog2)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.volumesCombo.addItem(l.name())
  
    def save_location_dialog1(self):
        location = QtGui.QFileDialog.getSaveFileName(None, 'Shapefile file:', self.ui.volumesLayerPath.text(), 'Shp (*.shp);; All files (*)')
        if len(location) > 0:
            self.ui.volumesLayerPath.setText(location)

    def save_location_dialog2(self):
        location = QtGui.QFileDialog.getSaveFileName(None, 'Shapefile file:', self.ui.buildingLayerPath.text(), 'Shp (*.shp);; All files (*)')
        if len(location) > 0:
            self.ui.buildingLayerPath.setText(location)

    def building_layer_path(self):
        return self.ui.buildingLayerPath.text()

    def building_layer_name(self):
        return os.path.splitext(os.path.basename(self.ui.buildingLayerPath.text()))[0]
    
    def volumes_layer_path(self):
        return self.ui.volumesLayerPath.text()

    def volumes_layer_name(self):
        return os.path.splitext(os.path.basename(self.ui.volumesLayerPath.text()))[0]
    
    def input_layer_name(self):
        return str(self.ui.volumesCombo.currentText())
 
    def create_intersection_layer_check(self):
         return self.ui.intersectionLayerCheckBox.isChecked()

