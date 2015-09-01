from PyQt4 import QtCore, QtGui 
from Ui_Gjko import Ui_Gjko
# create the dialog for Gjko
class GjkoDialog(QtGui.QDialog):
  def __init__(self): 
    QtGui.QDialog.__init__(self) 
    # Set up the user interface from Designer. 
    self.ui = Ui_Gjko ()
    self.ui.setupUi(self)
