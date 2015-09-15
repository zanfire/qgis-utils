# import some modules used in the example
from qgis.core import *
from PyQt4 import QtCore, QtGui
import traceback
import time

def startWorker(self, layer):
    # create a new worker instance
    worker = Worker(layer)

    # configure the QgsMessageBar
    messageBar = self.iface.messageBar().createMessage('Doing something time consuming...', )
    progressBar = QtGui.QProgressBar()
    progressBar.setAlignment(QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
    cancelButton = QtGui.QPushButton()
    cancelButton.setText('Cancel')
    cancelButton.clicked.connect(worker.kill)
    messageBar.layout().addWidget(progressBar)
    messageBar.layout().addWidget(cancelButton)
    self.iface.messageBar().pushWidget(messageBar, self.iface.messageBar().INFO)
    self.messageBar = messageBar

    # start the worker in a new thread
    thread = QtCore.QThread(self)
    worker.moveToThread(thread)
    worker.finished.connect(workerFinished)
    worker.error.connect(workerError)
    worker.progress.connect(progressBar.setValue)
    thread.started.connect(worker.run)
    thread.start()
    self.thread = thread
    self.worker = worker


def workerFinished(self, ret):
    # clean up the worker and thread
    self.worker.deleteLater()
    self.thread.quit()
    self.thread.wait()
    self.thead.deleteLater()
    # remove widget from message bar
    self.iface.messageBar().popWidget(self.messageBar)
    if ret is not None:
        # report the result
        layer, total_area = ret
        self.iface.messageBar().pushMessage('The total area of {name} is {area}.'.format(name=layer.name(), area=total_area))
    else:
        # notify the user that something went wrong
        self.iface.messageBar().pushMessage('Something went wrong! See the message log for more information.', level=QgsMessageBar.CRITICAL, duration=3)

def workerError(self, e, exception_string):
    QgsMessageLog.logMessage('Worker thread raised an exception:\n'.format(exception_string), level=QgsMessageLog.CRITICAL)
        

class Worker(QtCore.QObject):
    '''Example worker for calculating the total area of all features in a layer'''
    def __init__(self, Action):
        QtCore.QObject.__init__(self)
        if isinstance(layer, QgsVectorLayer) is False:
             raise TypeError('Worker expected a QgsVectorLayer, got a {} instead'.format(type(layer)))
        self.layer = layer
        self.killed = False

        self.finished = QtCore.pyqtSignal(object)
        self.error = QtCore.pyqtSignal(Exception, basestring)
        self.progress = QtCore.pyqtSignal(float)

    def run(self):
        ret = None
        try:
            # calculate the total area of all of the features in a layer
            total_area = 0.0
            features = self.layer.getFeatures()
            feature_count = self.layer.featureCount()
            progress_count = 0
            step = feature_count // 1000
            for feature in features:
                if self.killed is True:
                    # kill request received, exit loop early
                    break
                geom = feature.geometry()
                total_area += geom.area()
                time.sleep(0.1) # simulate a more time consuming task
                # increment progress
                progress_count += 1
                if step == 0 or progress_count % step == 0:
                    self.progress.emit(progress_count / float(feature_count))
                    if self.killed is False:
                        self.progress.emit(100)
                ret = (self.layer, total_area,)
        except Exception, e:
            self.error.emit(e, traceback.format_exc())
            self.finished.emit(ret)

    def kill(self):
        self.killed = True

