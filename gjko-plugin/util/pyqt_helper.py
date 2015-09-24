from qgis.core import *
from PyQt4 import QtCore, QtGui
import traceback
import time

def create_progress_bar(iface, message, worker):
    """
    This function retrun a dialog with a progress par.
    """
    messageBar = iface.messageBar().createMessage(message)
    progressBar = QtGui.QProgressBar()
    progressBar.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    #cancelButton = QtGui.QPushButton()
    #cancelButton.setText('Cancel')
    #cancelButton.clicked.connect(worker.kill)
    messageBar.layout().addWidget(progressBar)
    #messageBar.layout().addWidget(cancelButton)
    iface.messageBar().pushWidget(messageBar, iface.messageBar().INFO)
    return (messageBar, progressBar)
