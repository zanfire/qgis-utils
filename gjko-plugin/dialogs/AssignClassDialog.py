from PyQt4 import QtCore, QtGui
from qgis.utils import iface
from Ui_AssignClass import Ui_Dialog
import os

def helper_selectcombo(combo, text):
    index = combo.findText(text, QtCore.Qt.MatchContains)
    if index >= 0:
        combo.setCurrentIndex(index)

class AssignClassDialog(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        layers = iface.legendInterface().layers()
        for l in layers:
            name = l.name()
            self.ui.volumesCombo.addItem(name)
            self.ui.buildingCombo.addItem(name)
            self.ui.istatCombo.addItem(name)
        # Guess data for convenience.
        helper_selectcombo(self.ui.volumesCombo, "volume")
        helper_selectcombo(self.ui.buildingCombo, "build")
        helper_selectcombo(self.ui.istatCombo, "istat")

        QtCore.QObject.connect(self.ui.epcOpenButton, QtCore.SIGNAL('clicked()'), self.epc_open_file)
        QtCore.QObject.connect(self.ui.typologyOpenButton, QtCore.SIGNAL('clicked()'), self.typology_open_file)
        QtCore.QObject.connect(self.ui.istatOpenButton, QtCore.SIGNAL('clicked()'), self.istat_open_file)


    def volumes_layer_name(self):
       return str(self.ui.volumesCombo.currentText())

    def building_layer_name(self):
       return str(self.ui.buildingCombo.currentText())
   
    def epcs_csv_file(self):
        return self.ui.epcEdit.text()
    
    def typology_csv_file(self):
        return self.ui.typologyEdit.text()

    def istat_csv_file(self):
        return self.ui.istatEdit.text()

    def istat_layer_name(self):
        return str(self.ui.istatCombo.currentText())

    def epc_open_file(self):
        f = self.open_file()
        self.ui.epcEdit.setText(f)

    def typology_open_file(self):
        f = self.open_file()
        self.ui.typologyEdit.setText(f)

    def istat_open_file(self):
        f = self.open_file()
        self.ui.istatEdit.setText(f)

    def open_file(self):
        location = QtGui.QFileDialog.getOpenFileName(None, 'Open CSV file:', os.getenv('HOME'), 'CSV (*.csv);; All files (*)')
        return location

