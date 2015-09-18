from PyQt4 import QtCore, QtGui
from qgis.utils import iface
from Ui_AssignClass import Ui_Dialog
import os

class AssignClassDialog(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.energyCombo.addItem(l.name())
            self.ui.istatCombo.addItem(l.name())
        QtCore.QObject.connect(self.ui.epcOpenButton, QtCore.SIGNAL('clicked()'), self.epc_open_file)
        QtCore.QObject.connect(self.ui.istatOpenButton, QtCore.SIGNAL('clicked()'), self.istat_open_file)

    def energy_layer_name(self):
       return str(self.ui.energyCombo.currentText())

    def certificate_layer_name(self):
        return str(self.ui.certificateCombo.currentText())

    def epcs_csv_file(self):
        return self.ui.epcEdit.text()

    def istat_csv_file(self):
        return self.ui.istatEdit.text()

    def istat_layer_name(self):
        return str(self.ui.istatCombo.currentText())

    #def create_intersection_layer_check(self):
    #     return self.ui.intersectionLayerCheckBox.isChecked()

    def epc_open_file(self):
        f = self.open_file()
        self.ui.epcEdit.setText(f)

    def istat_open_file(self):
        f = self.open_file()
        self.ui.istatEdit.setText(f)

    def open_file(self):
        location = QtGui.QFileDialog.getOpenFileName(None, 'Open CSV file:', os.getenv('HOME'), 'CSV (*.csv);; All files (*)')
        return location

