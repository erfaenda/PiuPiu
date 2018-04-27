import sys
# Импортируем наш интерфейс из файла
from PyQTT.Gpio_control.gpio_gui_child import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Child(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # slots
        #self.ui.pushButton.clicked.connect(self.save_events)
        #self.ui.returnPressed()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Any:
            print('Click')

