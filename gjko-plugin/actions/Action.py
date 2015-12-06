# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
from ..util import pyqt_helper
from ..resources import *
import traceback
import time

class Worker(QtCore.QObject):
  
    finished = QtCore.pyqtSignal(object)
    error = QtCore.pyqtSignal(Exception, basestring)
    progress = QtCore.pyqtSignal(float)
    inerror = False

    def __init__(self, action):
        QtCore.QObject.__init__(self)
        self.action = action
        self.killed = False

    def process(self):
        try:
            QgsMessageLog.logMessage("Starting processing ...")
            self.action.initialize()
            #time.sleep(2) # simulate a more time consuming task
            #self.progress.emit(55)
            #time.sleep(2)
            self.action.compute(self.progress)
            QgsMessageLog.logMessage("Terminated processing ...")
        except Exception, e:
            self.inerror = True
            self.error.emit(e, traceback.format_exc())
        self.finished.emit(None)

    def kill(self):
        self.killed = True


class Action(object):
    """
    Define the abstract implementation of an action.
    """
    #dlg = None

    def __init__(self, iface, menu_name, name):
        self.iface = iface
        self.menu = menu_name
        self.action = QAction(QIcon(":/plugins/Gjko/icon.png"), name, self.iface.mainWindow())
        QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    def load(self):  
        #self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(self.menu, self.action)

    def unload(self):
        self.iface.removePluginMenu(self.menu, self.action)
        #self.iface.removeToolBarIcon(self.action)

    def create_dialog(self):
        return None
    
    def initialize(self):
        return

    def compute(self, progress):
        return

    def run(self):
        self.dlg = self.create_dialog()
        if self.dlg == None:
            QgsMessageLog.logMessage("No dialog available!")
            # Message an error due to missing implementation.
            return
        self.dlg.show()
        result = self.dlg.exec_() 
        if result == 1:
            self.start_worker()
            #self.apply()


    def start_worker(self):
        # create a new worker instance
        worker = Worker(self)
        
        (self.message_bar, progressBar) = pyqt_helper.create_progress_bar(self.iface, "Computing information ...", worker)
        # start the worker in a new thread
        thread = QtCore.QThread(worker)
        worker.moveToThread(thread)
        
        worker.finished.connect(self.worker_finished)
        worker.error.connect(self.worker_error)
        worker.progress.connect(progressBar.setValue)
        
        thread.started.connect(worker.process)
        thread.start()
        self.thread = thread
        self.worker = worker


    def worker_finished(self, ret):
        # clean up the worker and thread
        ##self.worker.deleteLater()
        #self.thread.quit()
        #self.thread.wait()
        #self.thead.deleteLater()
        # remove widget from message bar
        self.iface.messageBar().popWidget(self.message_bar)
        if not self.worker.inerror: 
            self.apply()

    def worker_error(self, e, exception_string): 
        QgsMessageLog.logMessage('Worker thread raised an exception:' + exception_string, level=QgsMessageLog.CRITICAL)
        self.iface.messageBar().pushMessage('An error was occurred, exception:' + str(e), QgsMessageBar.CRITICAL)

