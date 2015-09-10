# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/Ui_ComputeCompactRatio.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 392)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 371))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.volumesCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumesCombo.sizePolicy().hasHeightForWidth())
        self.volumesCombo.setSizePolicy(sizePolicy)
        self.volumesCombo.setObjectName(_fromUtf8("volumesCombo"))
        self.verticalLayout.addWidget(self.volumesCombo)
        self.onlySelectedCheckbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.onlySelectedCheckbox.setEnabled(False)
        self.onlySelectedCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.onlySelectedCheckbox.setChecked(True)
        self.onlySelectedCheckbox.setObjectName(_fromUtf8("onlySelectedCheckbox"))
        self.verticalLayout.addWidget(self.onlySelectedCheckbox)
        self.simplifyLayerCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.simplifyLayerCheckBox.setChecked(True)
        self.simplifyLayerCheckBox.setObjectName(_fromUtf8("simplifyLayerCheckBox"))
        self.verticalLayout.addWidget(self.simplifyLayerCheckBox)
        self.intersectionLayerCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.intersectionLayerCheckBox.setChecked(False)
        self.intersectionLayerCheckBox.setObjectName(_fromUtf8("intersectionLayerCheckBox"))
        self.verticalLayout.addWidget(self.intersectionLayerCheckBox)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.layerName = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.layerName.setObjectName(_fromUtf8("layerName"))
        self.verticalLayout.addWidget(self.layerName)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.saveFolder = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.saveFolder.setEnabled(False)
        self.saveFolder.setObjectName(_fromUtf8("saveFolder"))
        self.verticalLayout.addWidget(self.saveFolder)
        self.locationButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.locationButton.setEnabled(False)
        self.locationButton.setObjectName(_fromUtf8("locationButton"))
        self.verticalLayout.addWidget(self.locationButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalLayoutWidget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "Volumes layer:", None))
        self.onlySelectedCheckbox.setText(_translate("Dialog", "Use only selected features in cartograpy layer", None))
        self.simplifyLayerCheckBox.setText(_translate("Dialog", "Create simplified layer", None))
        self.intersectionLayerCheckBox.setText(_translate("Dialog", "Create interesection layer", None))
        self.label_3.setText(_translate("Dialog", "Layer name:", None))
        self.layerName.setText(_translate("Dialog", "Energy_values", None))
        self.label_4.setText(_translate("Dialog", "Save here:", None))
        self.locationButton.setText(_translate("Dialog", "Location", None))

