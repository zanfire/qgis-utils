from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_ComputeCompactRatio import Ui_Dialog

class ComputeCompactRatioDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #QtCore.QObject.connect(self.ui.locationButton, QtCore.SIGNAL('clicked()'), self.openLocation)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.inputLayer.addItem(l.name())
            self.ui.targetLayer.addItem(l.name())
 
    def inputLayer(self):
        return str(self.ui.inputLayer.currentText())

    def targetLayer(self):
        return str(self.ui.targetLayer.currentText())

