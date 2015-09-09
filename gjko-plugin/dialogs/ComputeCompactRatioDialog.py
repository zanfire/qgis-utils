from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_ComputeCompactRatio import Ui_Dialog

class ComputeCompactRatioDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.locationButton, QtCore.SIGNAL('clicked()'), self.openLocation)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.volumesCombo.addItem(l.name())
 
    
    def openLocation(self):
        location = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QtGui.QFileDialog.ShowDirsOnly)
        self.ui.saveFolder.setText(location)

    def working_layer_name(self):
        return self.ui.layerName.text()
    
    def location(self):
        return self.ui.saveFolder.text()
   
    def simplifyLayerCheck(self):
        return self.ui.simplifyLayerCheckBox.isChecked()

    def volumes_layer_name(self):
        return str(self.ui.volumesCombo.currentText())

    def create_intersection_layer_check(self):
         return self.ui.intersectionLayerCheckBox.isChecked()

