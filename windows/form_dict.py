# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/dict.ui'
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
        dict_form.resize(504, 318)
        self.horizontalLayout = QtGui.QHBoxLayout(dict_form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dict_view = QtGui.QListWidget(dict_form)
        self.dict_view.setMinimumSize(QtCore.QSize(300, 300))
        self.dict_view.setObjectName(_fromUtf8("dict_view"))
        self.horizontalLayout.addWidget(self.dict_view)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.search_line = QtGui.QLineEdit(dict_form)
        self.search_line.setMaximumSize(QtCore.QSize(300, 16777215))
        self.search_line.setObjectName(_fromUtf8("search_line"))
        self.verticalLayout.addWidget(self.search_line)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.add_button = QtGui.QPushButton(dict_form)
        self.add_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.add_button.setObjectName(_fromUtf8("add_button"))
        self.gridLayout.addWidget(self.add_button, 1, 0, 1, 1)
        self.save_button = QtGui.QPushButton(dict_form)
        self.save_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.save_button.setObjectName(_fromUtf8("save_button"))
        self.gridLayout.addWidget(self.save_button, 0, 0, 1, 1)
        self.undo_button = QtGui.QPushButton(dict_form)
        self.undo_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.undo_button.setObjectName(_fromUtf8("undo_button"))
        self.gridLayout.addWidget(self.undo_button, 1, 1, 1, 1)
        self.sort_button = QtGui.QPushButton(dict_form)
        self.sort_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sort_button.setObjectName(_fromUtf8("sort_button"))
        self.gridLayout.addWidget(self.sort_button, 0, 1, 1, 1)
        self.exit_button = QtGui.QPushButton(dict_form)
        self.exit_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.exit_button.setObjectName(_fromUtf8("exit_button"))
        self.gridLayout.addWidget(self.exit_button, 2, 1, 1, 1)
        self.delete_button = QtGui.QPushButton(dict_form)
        self.delete_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.gridLayout.addWidget(self.delete_button, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(dict_form)
        QtCore.QMetaObject.connectSlotsByName(dict_form)

    def retranslateUi(self, dict_form):
        dict_form.setWindowTitle(_translate("dict_form", "Dictionary", None))
        self.add_button.setText(_translate("dict_form", "Add", None))
        self.save_button.setText(_translate("dict_form", "Save", None))
        self.undo_button.setText(_translate("dict_form", "Undo", None))
        self.sort_button.setText(_translate("dict_form", "Sort", None))
        self.exit_button.setText(_translate("dict_form", "Exit", None))
        self.delete_button.setText(_translate("dict_form", "Delete", None))

