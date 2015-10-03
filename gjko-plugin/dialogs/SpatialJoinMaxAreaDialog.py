from PyQt4 import QtCore, QtGui 
from qgis.utils import iface
from Ui_SpatialJoinMaxArea import Ui_Dialog
from ..util import layer_helper
import os

class SpatialJoinMaxAreaDialog(QtGui.QDialog):

    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.layerName.setText(os.path.join(os.getenv('HOME'), "SpatialJoinMaxArea.shp"))
        QtCore.QObject.connect(self.ui.locationButton, QtCore.SIGNAL('clicked()'), self.save_location_dialog)
        QtCore.QObject.connect(self.ui.layer2Combo, QtCore.SIGNAL('currentIndexChanged(QString)'), self.on_layer_changed)
        layers = iface.legendInterface().layers()
        for l in layers:
            self.ui.layer1Combo.addItem(l.name())
            self.ui.layer2Combo.addItem(l.name())
        #self.ui.cadastreTerrainCombo.addItem(l.name())

    def save_location_dialog(self):
        location = QtGui.QFileDialog.getSaveFileName(None, 'Shapefile file:', self.ui.layerName.text(), 'Shp (*.shp);; All files (*)')
        if len(location) > 0:
            self.ui.layerName.setText(location)
    
    def location(self):
        return self.ui.layerName.text()
    
    def layer1_layer_name(self):
        return str(self.ui.layer1Combo.currentText())

    def layer2_layer_name(self):
        return str(self.ui.layer2Combo.currentText())

    def field_name(self):
        return str(self.ui.fieldCombo.currentText())

    def on_layer_changed(self):
        self.ui.fieldCombo.clear();
        layer = layer_helper.get_layer(self.layer2_layer_name())
        for attr in layer.pendingFields():
            self.ui.fieldCombo.addItem(attr.name())
