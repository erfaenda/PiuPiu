import sys
# Импортируем наш интерфейс из файла
from PyQTT.Complitter.guiComplitter import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt
class MyWin(QtWidgets.QMainWindow):

    spisok = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Add)
        self.ui.lineEdit.textEdited.connect(self.ViewPlainText)

    def Add(self):
        text = self.ui.lineEdit.text()
        spisok = str(self.spisok)

        if spisok.find(text) == -1:
            self.spisok.append(text)
            self.ViewPlainText()
        return

    def ViewPlainText(self):
        self.ui.plainTextEdit.setPlainText(str(self.spisok))

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())