# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dict.ui'
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

class Ui_dict_form(object):
    def setupUi(self, dict_form):
        dict_form.setObjectName(_fromUtf8("dict_form"))
        dict_form.resize(633, 379)
        self.search_line = QtGui.QLineEdit(dict_form)
        self.search_line.setGeometry(QtCore.QRect(350, 30, 271, 32))
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.add_button = QtGui.QPushButton(dict_form)
        self.add_button.setGeometry(QtCore.QRect(400, 90, 91, 30))
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.delete_button = QtGui.QPushButton(dict_form)
        self.delete_button.setGeometry(QtCore.QRect(400, 140, 91, 30))
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.dict_view = QtGui.QListWidget(dict_form)
        self.dict_view.setGeometry(QtCore.QRect(10, 20, 331, 341))
        self.dict_view.setObjectName(_fromUtf8("dict_view"))
        self.undo_button = QtGui.QPushButton(dict_form)
        self.undo_button.setGeometry(QtCore.QRect(400, 240, 91, 30))
        self.undo_button.setObjectName(_fromUtf8("undo_button"))
        self.sort_button = QtGui.QPushButton(dict_form)
        self.sort_button.setGeometry(QtCore.QRect(400, 190, 91, 30))
        self.sort_button.setObjectName(_fromUtf8("sort_button"))
        self.save_button = QtGui.QPushButton(dict_form)
        self.save_button.setGeometry(QtCore.QRect(400, 290, 91, 30))
        self.save_button.setObjectName(_fromUtf8("save_button"))

        self.retranslateUi(dict_form)
        QtCore.QMetaObject.connectSlotsByName(dict_form)

    def retranslateUi(self, dict_form):
        dict_form.setWindowTitle(_translate("dict_form", "Form", None))
        self.add_button.setText(_translate("dict_form", "Add", None))
        self.delete_button.setText(_translate("dict_form", "Delete", None))
        self.undo_button.setText(_translate("dict_form", "Undo", None))
        self.sort_button.setText(_translate("dict_form", "Sort", None))
        self.save_button.setText(_translate("dict_form", "Exit", None))

