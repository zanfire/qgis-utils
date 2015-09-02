from qgis.utils import iface
from PyQt4 import QtCore, QtGui 
from Ui_ManualCheck import Ui_Dialog
from ..util import layer_helper

class ManualCheckDialog(QtGui.QDialog):
    def __init__(self): 
        QtGui.QDialog.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        # Fill data
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.layersCombo.addItem(l.name())

        QtCore.QObject.connect(self.ui.previousButton, QtCore.SIGNAL('clicked()'), self.onPrev)
        QtCore.QObject.connect(self.ui.currentButton, QtCore.SIGNAL('clicked()'), self.onCurrent)
        QtCore.QObject.connect(self.ui.nextButton, QtCore.SIGNAL('clicked()'), self.onNext)
        
        self.layerName = None

    def onNext(self):
        if self.layerName == None:
            self.initLayerNavigation()
        #if self.currentFeatureIdx >= len(self.features):
        #    return
 
        layer_helper.show_features(self.layer, [ self.features[self.currentFeatureIdx]])
        self.currentFeatureIdx += 1

    def onCurrent(self):
        if self.layerName == None:
            return
        if self.currentFeatureIdx < 0:
            return
        layer_helper.show_features(self.layer, [ self.features[self.currentFeatureIdx - 1]])

    def onPrev(self):
        if self.layerName == None:
            return
        if self.currentFeatureIdx < 0:
            return
        layer_helper.show_features(self.layer, [ self.features[self.currentFeatureIdx]])
        self.currentFeatureIdx -= 1

    def initLayerNavigation(self):
        self.layerName = str(self.ui.layersCombo.currentText())
        self.layer = layer_helper.get_layer(self.layerName)
        idx = 0
        self.lenght = 0
        self.features = []
        for f in self.layer.getFeatures():
            self.features.append(f)
        self.currentFeatureIdx = 0
