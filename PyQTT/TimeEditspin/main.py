import sys
# Импортируем наш интерфейс из файла
from PyQTT.TimeEditspin.gui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        #self.ui.pushButton.clicked.connect(self.stroka_nasledovanya)
        self.ui.pushButton.clicked.connect(self.getTime)
        self.ui.pushButton.clicked.connect(self.checj)
        #self.ui.timeEdit_2.setTime(QtCore.QTime(4, int('01')))
        #PyQt5.QtCore.QTime(4, 0)
        self.ui.checkBox_2.setChecked(1)

    def getTime(self):
        time = self.ui.timeEdit.text()
        print(time)
        index = time.find(":")
        print(index)
        hour = time[:index]
        print(hour)

        minute = time[index + 1:]
        print(hour + " и " + minute)
        return hour, minute

    def checj(self):
        chk = self.ui.checkBox.isChecked()
        print(chk)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())