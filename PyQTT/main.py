import sys
# Импортируем наш интерфейс из файла
from PyQTT.testCheck import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.stroka_line)

    def list_line(self):
        list = []
        if self.ui.checkBox:
            list.append('(F)')
        if self.ui.checkBox_2.isChecked():
            list.append('(OI)')
        if self.ui.checkBox_3.isChecked():
            list.append('(CI)')
        print(list)
        return list

    def stroka_line(self):
        stroka = ''
        if self.ui.checkBox:
            stroka = stroka + '(F)'
        if self.ui.checkBox_2.isChecked():
            stroka = stroka + '(OI)'
        if self.ui.checkBox_3.isChecked():
            stroka = stroka + '(CI)'
        print(stroka)
        return stroka



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())