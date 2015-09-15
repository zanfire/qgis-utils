from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_Progress import Ui_Dialog

class ProgressDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    def set_max(self, max):
        self.max = max
        self.ui.label.setText('0 / ' + str(max))
        self.ui.progressBat.setMaximum(max)
    
    def set_current(self, current):
        self.ui.labelsetText(current + ' / ' + str(self.max))
        self.ui.progressBar.setValue(current)

