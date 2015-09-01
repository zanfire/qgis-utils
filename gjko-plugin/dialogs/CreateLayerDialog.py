from PyQt4 import QtCore, QtGui 
from Ui_CreateLayer import Ui_Dialog

class CreateLayerDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    self.ui = Ui_Dialog()
    self.ui.setupUi(self)
