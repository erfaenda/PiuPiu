import sys, os, time
# Импортируем наш интерфейс из файла
from PyQTT.Rasberry.controlGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.core_temp)


    def get_temp(self):
        temp = os.popen("vcgencmd measure_temp").readline()
        actual = str(234324234)
        self.ui.plainTextEdit.appendPlainText(actual)
        return actual#(temp.replace("temp=", ""))

    def core_temp(self):
        while True:
            print(self.get_temp())
            self.ui.plainTextEdit.appendPlainText(self.get_temp())
            time.sleep(1)


    # Пока пустая функция которая выполняется



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())