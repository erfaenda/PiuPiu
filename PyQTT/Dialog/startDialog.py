import sys
# Импортируем наш интерфейс из файла
from PyQTT.Dialog.dialogGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.actionExit.triggered.connect(self.close)


    # при нажатии на кнопку
    def myfunction(self):
        self.ui.label.setText("Длинна вашего текста {} символов(а)".format(len(self.ui.lineEdit.text())))

    # отслеживаю нажатие  ентера и выполняю функцию
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Enter:
            self.myfunction()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())