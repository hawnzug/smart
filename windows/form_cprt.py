# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/copyright.ui'
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

class Ui_copyright_form(object):
    def setupUi(self, copyright_form):
        copyright_form.setObjectName(_fromUtf8("copyright_form"))
        copyright_form.resize(280, 220)
        self.label = QtGui.QLabel(copyright_form)
        self.label.setGeometry(QtCore.QRect(30, 20, 261, 180))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(copyright_form)
        QtCore.QMetaObject.connectSlotsByName(copyright_form)

    def retranslateUi(self, copyright_form):
        copyright_form.setWindowTitle(_translate("copyright_form", "Copyright", None))
        self.label.setText(_translate("copyright_form", "Smart Segmentation\n\nDesigned By Smart Boys:\n\nZhuyang Wang\nPihe Hu\nChaoran Xu", None))

