# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/Ui_CreateLayer.ui'
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
        Dialog.resize(352, 167)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(-10, 120, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.locationButton = QtGui.QPushButton(Dialog)
        self.locationButton.setGeometry(QtCore.QRect(240, 80, 96, 32))
        self.locationButton.setObjectName(_fromUtf8("locationButton"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 50, 81, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.layerName = QtGui.QLineEdit(Dialog)
        self.layerName.setGeometry(QtCore.QRect(110, 20, 221, 21))
        self.layerName.setObjectName(_fromUtf8("layerName"))
        self.saveFolder = QtGui.QLineEdit(Dialog)
        self.saveFolder.setGeometry(QtCore.QRect(110, 50, 221, 21))
        self.saveFolder.setObjectName(_fromUtf8("saveFolder"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Create layer", None))
        self.locationButton.setText(_translate("Dialog", "Location", None))
        self.label.setText(_translate("Dialog", "Save here:", None))
        self.label_2.setText(_translate("Dialog", "Layer name:", None))

