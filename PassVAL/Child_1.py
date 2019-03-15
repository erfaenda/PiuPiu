import sys
# Импортируем наш интерфейс из файла
from PassVAL.guiChild_1 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class Child_1(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Child_1()
        self.ui.setupUi(self)

        # slots
        #self.ui.pushButton.clicked.connect(self.save_events)
        #self.ui.returnPressed()


