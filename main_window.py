# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
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

class Ui_smart_window(object):
    def setupUi(self, smart_window):
        smart_window.setObjectName(_fromUtf8("smart_window"))
        smart_window.resize(694, 481)
        self.centralwidget = QtGui.QWidget(smart_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.text_output = QtGui.QTextBrowser(self.centralwidget)
        self.text_output.setObjectName(_fromUtf8("text_output"))
        self.gridLayout.addWidget(self.text_output, 0, 1, 1, 1)
        self.text_input = QtGui.QTextEdit(self.centralwidget)
        self.text_input.setObjectName(_fromUtf8("text_input"))
        self.gridLayout.addWidget(self.text_input, 0, 0, 1, 1)
        self.seg_button = QtGui.QPushButton(self.centralwidget)
        self.seg_button.setMinimumSize(QtCore.QSize(0, 0))
        self.seg_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.seg_button.setObjectName(_fromUtf8("seg_button"))
        self.gridLayout.addWidget(self.seg_button, 1, 0, 1, 1)
        smart_window.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(smart_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 694, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        smart_window.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(smart_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        smart_window.setStatusBar(self.statusbar)

        self.retranslateUi(smart_window)
        QtCore.QMetaObject.connectSlotsByName(smart_window)

    def retranslateUi(self, smart_window):
        smart_window.setWindowTitle(_translate("smart_window", "Smart Segmentation", None))
        self.seg_button.setText(_translate("smart_window", "segment", None))

