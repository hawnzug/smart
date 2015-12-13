# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/instruction.ui'
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

class Ui_instruction_form(object):
    def setupUi(self, instruction_form):
        instruction_form.setObjectName(_fromUtf8("instruction_form"))
        instruction_form.resize(320, 240)
        self.label = QtGui.QLabel(instruction_form)
        self.label.setGeometry(QtCore.QRect(40, 30, 251, 171))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(instruction_form)
        QtCore.QMetaObject.connectSlotsByName(instruction_form)

    def retranslateUi(self, instruction_form):
        instruction_form.setWindowTitle(_translate("instruction_form", "Instruction", None))
        self.label.setText(_translate("instruction_form", "Instruction", None))

