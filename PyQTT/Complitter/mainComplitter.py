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
        self.ui.lineEdit.returnPressed.connect(self.Add)

    def Add(self):
        text = self.ui.lineEdit.text()
        Localspisok = str(self.spisok)

        if Localspisok.find(text) == -1:
            self.spisok.append(text)
            self.ViewPlainText()
            self.Compliteer()

        else:
            self.spisok.append(text + ' unicum')
            self.ViewPlainText()
            self.Compliteer()

    def ViewPlainText(self):
        self.ui.plainTextEdit.setPlainText(str(self.spisok))

    def Compliteer(self):
        # Создаём QCompleter, в который устанавливаем список, а также указатель на родителя
        completer = QCompleter(self.spisok, self.ui.lineEdit)
        self.ui.lineEdit.setCompleter(completer)  # Устанавливает QCompleter в поле ввода
        self.ui.gridLayout.addWidget(self.ui.lineEdit, 1, 0, 1, 1)  # Добавляем поле ввода в сетку

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())