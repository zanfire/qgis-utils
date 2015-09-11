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
        Dialog.resize(231, 140)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 216, 121))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.layersCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.layersCombo.setObjectName(_fromUtf8("layersCombo"))
        self.verticalLayout.addWidget(self.layersCombo)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.currentIndexText = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.currentIndexText.sizePolicy().hasHeightForWidth())
        self.currentIndexText.setSizePolicy(sizePolicy)
        self.currentIndexText.setMaximumSize(QtCore.QSize(100, 16777215))
        self.currentIndexText.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.currentIndexText.setObjectName(_fromUtf8("currentIndexText"))
        self.horizontalLayout_2.addWidget(self.currentIndexText)
        self.maxLabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxLabel.sizePolicy().hasHeightForWidth())
        self.maxLabel.setSizePolicy(sizePolicy)
        self.maxLabel.setObjectName(_fromUtf8("maxLabel"))
        self.horizontalLayout_2.addWidget(self.maxLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previousButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.previousButton.setAutoDefault(False)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.horizontalLayout.addWidget(self.previousButton)
        self.currentButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.currentButton.setObjectName(_fromUtf8("currentButton"))
        self.horizontalLayout.addWidget(self.currentButton)
        self.nextButton = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextButton.sizePolicy().hasHeightForWidth())
        self.nextButton.setSizePolicy(sizePolicy)
        self.nextButton.setFocusPolicy(QtCore.Qt.TabFocus)
        self.nextButton.setDefault(True)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.horizontalLayout.addWidget(self.nextButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Navigate", None))
        self.maxLabel.setText(_translate("Dialog", "TextLabel", None))
        self.previousButton.setText(_translate("Dialog", "<<", None))
        self.currentButton.setText(_translate("Dialog", "Current", None))
        self.nextButton.setText(_translate("Dialog", ">>", None))

