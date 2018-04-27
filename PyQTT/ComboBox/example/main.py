import sys
# Импортируем наш интерфейс из файла
from PyQTT.ComboBox.example.gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.main_func)

    def main_func(self):
        if self.ui.comboBox.currentIndex() == 0:
            self.func1()
        else:
            self.func2()

    def func1(self):
        self.ui.label.setText("Работает функция 1")

    def func2(self):
        self.ui.label.setText("Работает функция 2")


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())