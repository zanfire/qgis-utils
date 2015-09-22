from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_ComputeCompactRatio import Ui_Dialog
import os

class ComputeCompactRatioDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.locationButton, QtCore.SIGNAL('clicked()'), self.save_location_dialog)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.volumesCombo.addItem(l.name())
  
    def save_location_dialog(self):
        location = QtGui.QFileDialog.getSaveFileName(None, 'Shapefile file:', os.getenv('HOME'), 'Shp (*.shp);; All files (*)')
        #location = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QtGui.QFileDialog.ShowDirsOnly)
        self.ui.saveFolder.setText(location)

    def working_layer_name(self):
        return self.ui.layerName.text()
    
    def location(self):
        return self.ui.saveFolder.text()
   
    def keep_temporary_layer(self):
        return self.ui.keepTemporaryLayerCheckBox.isChecked()

    def volumes_layer_name(self):
        return str(self.ui.volumesCombo.currentText())

    def create_intersection_layer_check(self):
         return self.ui.intersectionLayerCheckBox.isChecked()

