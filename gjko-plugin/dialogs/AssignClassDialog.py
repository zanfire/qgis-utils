from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_AssignClass import Ui_Dialog

class AssignClassDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.energyCombo.addItem(l.name())
            self.ui.certificateCombo.addItem(l.name())
            self.ui.istatCombo.addItem(l.name())
    
    def energy_layer_name(self):
       return str(self.ui.energyCombo.currentText())
    
    def certificate_layer_name(self):
        return str(self.ui.certificateCombo.currentText())

    def istat_layer_name(self):
        return str(self.ui.istatCombo.currentText())

    #def create_intersection_layer_check(self):
    #     return self.ui.intersectionLayerCheckBox.isChecked()

