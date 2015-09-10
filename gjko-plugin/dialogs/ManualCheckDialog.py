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
        QtCore.QObject.connect(self.ui.previousButton, QtCore.SIGNAL('clicked()'), self.onPrev)
        QtCore.QObject.connect(self.ui.currentButton, QtCore.SIGNAL('clicked()'), self.onCurrent)
        QtCore.QObject.connect(self.ui.nextButton, QtCore.SIGNAL('clicked()'), self.onNext)
        QtCore.QObject.connect(self.ui.layersCombo, QtCore.SIGNAL('currentIndexChanged(QString)'), self.onLayerChanged)
        QtCore.QObject.connect(self.ui.currentIndexText, QtCore.SIGNAL('textEdited(QString)'), self.onIndexChanged)
 
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.layersCombo.addItem(l.name())
 
        self.layerName = None

    def onNext(self):
        if self.layerName == None:
            self.initLayerNavigation()
        if self.currentFeatureIdx >= (len(self.features) - 1):
            return
        self.currentFeatureIdx += 1
        self.ui.currentIndexText.setText(str(self.currentFeatureIdx + 1))
        layer_helper.show_features(self.layer, [ self.features[self.currentFeatureIdx]])

    def onCurrent(self):
        if self.layerName == None:
            return
        if self.currentFeatureIdx < 0:
            return
        layer_helper.show_features(self.layer, [ self.features[self.currentFeatureIdx]])
        self.ui.currentIndexText.setText(str(self.currentFeatureIdx + 1))     
 
    def onPrev(self):
        if self.layerName == None:
            return
        if self.currentFeatureIdx <= 0:
            return
        self.currentFeatureIdx -= 1
        layer_helper.show_features(self.layer, [ self.features[self.currentFeatureIdx]])
        self.ui.currentIndexText.setText(str(self.currentFeatureIdx + 1))     
    
    def onLayerChanged(self, name):
        self.initLayerNavigation()
        self.onCurrent()

    def onIndexChanged(self, value):
        if len(value) == 0:
            return
        if not str(value).isdigit():
            return
        intvalue = int(value) - 1
        if intvalue >= (len(self.features) - 1):
            return
 
        self.currentFeatureIdx = intvalue
        self.onCurrent()

    def initLayerNavigation(self):
        self.layerName = str(self.ui.layersCombo.currentText())
        self.layer = layer_helper.get_layer(self.layerName)
        iface.setActiveLayer(self.layer)
        self.features = []
        for f in self.layer.getFeatures():
            self.features.append(f)
        self.ui.maxLabel.setText(" of " + str(len(self.features)))
        self.currentFeatureIdx = 0
