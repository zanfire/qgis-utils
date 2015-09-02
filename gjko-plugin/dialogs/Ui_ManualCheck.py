# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/Ui_ManualCheck.ui'
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
        Dialog.resize(400, 183)
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 100, 401, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previousButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.horizontalLayout.addWidget(self.previousButton)
        self.currentButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.currentButton.setObjectName(_fromUtf8("currentButton"))
        self.horizontalLayout.addWidget(self.currentButton)
        self.nextButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.layersCombo = QtGui.QComboBox(Dialog)
        self.layersCombo.setGeometry(QtCore.QRect(10, 20, 381, 26))
        self.layersCombo.setObjectName(_fromUtf8("layersCombo"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.previousButton.setText(_translate("Dialog", "Previous", None))
        self.currentButton.setText(_translate("Dialog", "Current", None))
        self.nextButton.setText(_translate("Dialog", "Next", None))

