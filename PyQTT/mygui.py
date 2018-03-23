import sys
# Импортируем наш интерфейс из файла
from PyQTT.testGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        #self.ui.pushButton.clicked.connect(self.MyFunction)
        #self.widget.keyPressEvent2.connect(self.MyFunction)
        self.ui.pushButton.clicked.connect(self.clearAll)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку
    def clearAll(self):
        self.ui.buttonGroup.setExclusive(False)
        self.ui.radioButton.setChecked(False)
        self.ui.radioButton_2.setChecked(False)
        self.ui.radioButton_3.setChecked(False)
        self.ui.buttonGroup.setExclusive(True)



    def my_method(self):
        self.group.setExclusive(False)
        self.radiobutton1.setChecked(False)
        self.radiobutton2.setChecked(False)
        self.group.setExclusive(True)


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())