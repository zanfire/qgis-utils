from PyQt4 import QtCore, QtGui 
from Ui_CreateLayer import Ui_Dialog

class CreateLayerDialog(QtGui.QDialog):
    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.locationButton, QtCore.SIGNAL('clicked()'), self.openLocation)
    
    def openLocation(self):
        location = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', '', QtGui.QFileDialog.ShowDirsOnly)
        self.ui.saveFolder.setText(location)

    def name(self):
        return self.ui.layerName.text()
    
    def location(self):
        return self.ui.saveFolder.text()

