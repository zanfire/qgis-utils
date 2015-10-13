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
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.volumesLayerPath = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.volumesLayerPath.setText(_fromUtf8(""))
        self.volumesLayerPath.setObjectName(_fromUtf8("volumesLayerPath"))
        self.verticalLayout.addWidget(self.volumesLayerPath)
        self.locationButton1 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.locationButton1.setEnabled(True)
        self.locationButton1.setObjectName(_fromUtf8("locationButton1"))
        self.verticalLayout.addWidget(self.locationButton1)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.buildingLayerPath = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.buildingLayerPath.setEnabled(True)
        self.buildingLayerPath.setObjectName(_fromUtf8("buildingLayerPath"))
        self.verticalLayout.addWidget(self.buildingLayerPath)
        self.locationButton2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.locationButton2.setEnabled(True)
        self.locationButton2.setObjectName(_fromUtf8("locationButton2"))
        self.verticalLayout.addWidget(self.locationButton2)
        self.intersectionLayerCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.intersectionLayerCheckBox.setChecked(False)
        self.intersectionLayerCheckBox.setObjectName(_fromUtf8("intersectionLayerCheckBox"))
        self.verticalLayout.addWidget(self.intersectionLayerCheckBox)
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
        Dialog.setWindowTitle(_translate("Dialog", "2 - Create energy layers", None))
        self.label_2.setText(_translate("Dialog", "Input layer:", None))
        self.label_3.setText(_translate("Dialog", "Volumes layer:", None))
        self.locationButton1.setText(_translate("Dialog", "Location", None))
        self.label_4.setText(_translate("Dialog", "Building layer:", None))
        self.locationButton2.setText(_translate("Dialog", "Location", None))
        self.intersectionLayerCheckBox.setText(_translate("Dialog", "Create interesection layer (debug)", None))

