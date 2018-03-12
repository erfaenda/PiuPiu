import sys
# Импортируем наш интерфейс из файла
from PyQTT.gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        #self.ui.pushButton.clicked.connect(self.MyFunction)
        #self.widget.keyPressEvent2.connect(self.MyFunction)

    # Пока пустая функция которая выполняется
    # при нажатии на кнопку


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F5:
            self.close()

    def keyPressEvent2(self, e):
        if e.key() == Qt.Key_F6:
            self.MyFunction()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())