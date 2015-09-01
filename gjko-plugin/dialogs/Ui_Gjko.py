# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/Ui_Gjko.ui'
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

class Ui_Gjko(object):
    def setupUi(self, Gjko):
        Gjko.setObjectName(_fromUtf8("Gjko"))
        Gjko.resize(389, 281)
        self.buttonBox = QtGui.QDialogButtonBox(Gjko)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.comboBox = QtGui.QComboBox(Gjko)
        self.comboBox.setGeometry(QtCore.QRect(200, 20, 181, 26))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.retranslateUi(Gjko)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Gjko.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Gjko.reject)
        QtCore.QMetaObject.connectSlotsByName(Gjko)

    def retranslateUi(self, Gjko):
        Gjko.setWindowTitle(_translate("Gjko", "Gjko", None))

