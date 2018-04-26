import sys
# Импортируем наш интерфейс из файла
from PyQTT.Gpio_control.gpio_gui_child import *
from PyQTT.Gpio_control.gpio_gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Child(QtWidgets.QMainWindow):

    line_1 = 'ЛОЛ'

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui_main = Ui_MainWindow()

        # slots
        self.ui.pushButton.clicked.connect(self.Save_change)

    def Save_change(self):
        self.line_1 = self.ui.lineEdit.text()
        return self.line_1




