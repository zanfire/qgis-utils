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
        Dialog.resize(401, 270)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(False)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 255))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.energyCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.energyCombo.sizePolicy().hasHeightForWidth())
        self.energyCombo.setSizePolicy(sizePolicy)
        self.energyCombo.setObjectName(_fromUtf8("energyCombo"))
        self.verticalLayout.addWidget(self.energyCombo)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.certificateCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.certificateCombo.sizePolicy().hasHeightForWidth())
        self.certificateCombo.setSizePolicy(sizePolicy)
        self.certificateCombo.setObjectName(_fromUtf8("certificateCombo"))
        self.verticalLayout.addWidget(self.certificateCombo)
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
        self.simplifyLayerCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.simplifyLayerCheckBox.setEnabled(False)
        self.simplifyLayerCheckBox.setChecked(True)
        self.simplifyLayerCheckBox.setObjectName(_fromUtf8("simplifyLayerCheckBox"))
        self.verticalLayout.addWidget(self.simplifyLayerCheckBox)
        self.intersectionLayerCheckBox = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.intersectionLayerCheckBox.setEnabled(False)
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
        Dialog.setWindowTitle(_translate("Dialog", "Assign class", None))
        self.label_4.setText(_translate("Dialog", "Energy values layer:", None))
        self.label_2.setText(_translate("Dialog", "Energy certification layer:", None))
        self.label_3.setText(_translate("Dialog", "ISTAT layer:", None))
        self.simplifyLayerCheckBox.setText(_translate("Dialog", "Create simplified layer", None))
        self.intersectionLayerCheckBox.setText(_translate("Dialog", "Create interesection layer", None))

