import sys
# Импортируем наш интерфейс из файла
from PyQTT.GuessWord.gwGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox.addItems('4 5'.split())
        self.ui.statusbar.showMessage('© Alexey Silantyev, 2018')

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.start1)

    # мои функции
    def start1(self):
        if self.ui.comboBox.currentIndex() == 0:
            self.wordFour(self.ui.lineEdit.text())
        elif self.ui.comboBox.currentIndex() == 1:
            self.wordFive(self.ui.lineEdit.text())

    def wordFour(self, letters):
        self.t1


    def wordFive(self):
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())