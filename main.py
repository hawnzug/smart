# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui
from windows.main_window import Ui_smart_window
from windows.form_dict import Ui_dict_form
from windows.form_inst import Ui_instruction_form
from windows.form_cprt import Ui_copyright_form
import segment


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_smart_window()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.seg_button, QtCore.SIGNAL('clicked()'), self.segment)

        action_open = QtGui.QAction('Open', self)
        self.connect(action_open, QtCore.SIGNAL('triggered()'), self.file_open)
        action_save_input = QtGui.QAction('Save input', self)
        self.connect(action_save_input, QtCore.SIGNAL('triggered()'), self.file_save_input)
        action_save_output = QtGui.QAction('Save output', self)
        self.connect(action_save_output, QtCore.SIGNAL('triggered()'), self.file_save_output)
        action_exit = QtGui.QAction('Exit', self)
        self.connect(action_exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))

        menu_file = self.ui.menubar.addMenu('&File')
        menu_file.addAction(action_open)
        menu_file.addAction(action_save_input)
        menu_file.addAction(action_save_output)
        menu_file.addAction(action_exit)

        action_handle_dict = QtGui.QAction('Edit', self)
        self.connect(action_handle_dict, QtCore.SIGNAL('triggered()'), self.handle_dict)

        menu_lexicon = self.ui.menubar.addMenu('&Dict')
        menu_lexicon.addAction(action_handle_dict)

        action_instruction = QtGui.QAction('Instruction', self)
        self.connect(action_instruction, QtCore.SIGNAL('triggered()'), self.instruction)
        action_copyright = QtGui.QAction('Copyright', self)
        self.connect(action_copyright, QtCore.SIGNAL('triggered()'), self.copyright)

        menu_help = self.ui.menubar.addMenu('&Help')
        menu_help.addAction(action_instruction)
        menu_help.addAction(action_copyright)

    def file_open(self):
        self.filename = QtGui.QFileDialog(self).getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            text = open(self.filename, 'r', encoding='utf-8').read()
            self.ui.text_input.setText(text)

    def file_save_input(self):
        self.filename = QtGui.QFileDialog(self).getSaveFileName()
        file_ = open(self.filename, 'w', encoding='utf-8')
        file_.write(self.ui.text_input.toPlainText())
        file_.close

    def file_save_output(self):
        self.filename = QtGui.QFileDialog(self).getSaveFileName()
        file_ = open(self.filename, 'w', encoding='utf-8')
        file_.write(self.ui.text_output.toPlainText())
        file_.close

    def segment(self):
        string = self.ui.text_input.toPlainText()
        self.ui.text_output.setText('|'.join(segment.main(string)))

    def handle_dict(self):
        self.dictform = DictForm()
        self.dictform.show()

    def instruction(self):
        self.instform = InstForm()
        self.instform.show()

    def copyright(self):
        self.cprtform = CprtForm()
        self.cprtform.show()


class DictForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_dict_form()
        self.ui.setupUi(self)
        self.undo_list = []

        QtCore.QObject.connect(self.ui.add_button, QtCore.SIGNAL('clicked()'), self.add)
        QtCore.QObject.connect(self.ui.delete_button, QtCore.SIGNAL('clicked()'), self.delete)
        QtCore.QObject.connect(self.ui.sort_button, QtCore.SIGNAL('clicked()'), self.sort)
        QtCore.QObject.connect(self.ui.undo_button, QtCore.SIGNAL('clicked()'), self.undo)
        QtCore.QObject.connect(self.ui.save_button, QtCore.SIGNAL('clicked()'), self.save)
        QtCore.QObject.connect(self.ui.exit_button, QtCore.SIGNAL('clicked()'), self.close)
        QtCore.QObject.connect(self.ui.search_line, QtCore.SIGNAL('textEdited(const QString&)'), self.search)

        self.ui.undo_button.setEnabled(False)
        self.ui.delete_button.setEnabled(False)
        self.ui.add_button.setEnabled(False)
        self.ui.save_button.setEnabled(False)
        lexicon = segment.mmseg.list_all()
        self.ui.dict_view.addItems(lexicon)
        self.ui.dict_view.itemClicked.connect(self.select)

    def select(self):
        self.ui.search_line.setText(self.ui.dict_view.currentItem().text())
        self.ui.delete_button.setEnabled(True)
        self.ui.add_button.setEnabled(False)
       
    def search(self):
        word = self.ui.search_line.text().strip()
        if segment.mmseg.trie_search(word) != -1:
            item = self.ui.dict_view.findItems(word, QtCore.Qt.MatchExactly)[0]
            self.ui.dict_view.scrollToItem(item)
            self.ui.dict_view.setCurrentItem(item)
            self.ui.delete_button.setEnabled(True)
            self.ui.add_button.setEnabled(False)
        else:
            self.ui.dict_view.clearSelection()
            self.ui.delete_button.setEnabled(False)
            if word != '':
                self.ui.add_button.setEnabled(True)
            else:
                self.ui.add_button.setEnabled(False)

    def add(self):
        word = self.ui.search_line.text().strip()
        if word != '' and segment.mmseg.trie_add(word, 1000):
            item = QtGui.QListWidgetItem()
            item.setText(word)
            self.ui.dict_view.addItem(item)
            self.ui.dict_view.scrollToItem(item)
            self.ui.dict_view.setCurrentItem(item)
            self.ui.undo_button.setEnabled(True)
            self.undo_list.append((item, False))
            self.ui.delete_button.setEnabled(True)
            self.ui.add_button.setEnabled(False)
            self.ui.sort_button.setEnabled(True)
            self.ui.save_button.setEnabled(True)
            self.ui.exit_button.setEnabled(False)

    def delete(self):
        item = self.ui.dict_view.currentItem()
        word = item.text()
        if word != '' and segment.mmseg.trie_delete(word):
            self.undo_list.append((item, True))
            self.ui.dict_view.takeItem(self.ui.dict_view.currentRow())
            self.ui.undo_button.setEnabled(True)
            self.ui.delete_button.setEnabled(False)
            self.ui.add_button.setEnabled(True)
            self.ui.dict_view.clearSelection()
            self.ui.save_button.setEnabled(True)
            self.ui.exit_button.setEnabled(False)

    def undo(self):
        item, flag = self.undo_list.pop()
        if flag:
            segment.mmseg.trie_add(item.text(), 1000)
            self.ui.dict_view.addItem(item)
            self.ui.dict_view.scrollToItem(item)
            self.ui.dict_view.setCurrentItem(item)
            self.ui.search_line.setText(item.text())
            self.ui.delete_button.setEnabled(True)
            self.ui.add_button.setEnabled(False)
            if self.undo_list == []:
                self.ui.undo_button.setEnabled(False)
            self.ui.sort_button.setEnabled(True)
        else:
            segment.mmseg.trie_delete(item.text())
            self.ui.dict_view.takeItem(self.ui.dict_view.indexFromItem(item).row())
            self.ui.search_line.setText(item.text())
            self.ui.delete_button.setEnabled(False)
            self.ui.add_button.setEnabled(True)
            self.ui.dict_view.clearSelection()
            if self.undo_list == []:
                self.ui.undo_button.setEnabled(False)
        if self.undo_list == []:
            self.ui.save_button.setEnabled(False)
            self.ui.exit_button.setEnabled(True)

    def sort(self):
        item = self.ui.dict_view.currentItem()
        self.ui.dict_view.sortItems()
        self.ui.dict_view.scrollToItem(item)
        self.ui.dict_view.setCurrentItem(item)
        self.ui.sort_button.setEnabled(False)

    def save(self):
        segment.mmseg.dict_update('resultA.py')
        self.ui.exit_button.setEnabled(True)


class InstForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_instruction_form()
        self.ui.setupUi(self)


class CprtForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_copyright_form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
