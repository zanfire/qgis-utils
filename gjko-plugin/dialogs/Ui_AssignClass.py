# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogs/Ui_AssignClass.ui'
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
        Dialog.resize(401, 394)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 385))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.volumesCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volumesCombo.sizePolicy().hasHeightForWidth())
        self.volumesCombo.setSizePolicy(sizePolicy)
        self.volumesCombo.setObjectName(_fromUtf8("volumesCombo"))
        self.verticalLayout.addWidget(self.volumesCombo)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.buildingCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buildingCombo.sizePolicy().hasHeightForWidth())
        self.buildingCombo.setSizePolicy(sizePolicy)
        self.buildingCombo.setObjectName(_fromUtf8("buildingCombo"))
        self.verticalLayout.addWidget(self.buildingCombo)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.epcEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.epcEdit.setObjectName(_fromUtf8("epcEdit"))
        self.verticalLayout.addWidget(self.epcEdit)
        self.epcOpenButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.epcOpenButton.setObjectName(_fromUtf8("epcOpenButton"))
        self.verticalLayout.addWidget(self.epcOpenButton)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.istatCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.istatCombo.sizePolicy().hasHeightForWidth())
        self.istatCombo.setSizePolicy(sizePolicy)
        self.istatCombo.setObjectName(_fromUtf8("istatCombo"))
        self.verticalLayout.addWidget(self.istatCombo)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.istatEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.istatEdit.setObjectName(_fromUtf8("istatEdit"))
        self.verticalLayout.addWidget(self.istatEdit)
        self.istatOpenButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.istatOpenButton.setObjectName(_fromUtf8("istatOpenButton"))
        self.verticalLayout.addWidget(self.istatOpenButton)
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
        Dialog.setWindowTitle(_translate("Dialog", "3 - Assign EPC and Typology", None))
        self.label_4.setText(_translate("Dialog", "Volumes layer:", None))
        self.label_6.setText(_translate("Dialog", "Building layer:", None))
        self.label_2.setText(_translate("Dialog", "EPCs CSV file:", None))
        self.epcOpenButton.setText(_translate("Dialog", "Select file", None))
        self.label_3.setText(_translate("Dialog", "ISTAT layer:", None))
        self.label_5.setText(_translate("Dialog", "ISTAT CSV file:", None))
        self.istatOpenButton.setText(_translate("Dialog", "Select file", None))

