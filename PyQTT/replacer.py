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
        self.ui.pushButton.clicked.connect(self.nasled)
        #self.ui.pushButton.clicked.connect(self.stroka_nasledovanya)

    def nasled(self):
        stroka = ''
        if self.ui.checkBox.isChecked():
            stroka = stroka + 'WA,'
        if self.ui.checkBox_2.isChecked():
            stroka = stroka + 'RC,'
        print('(' + stroka[0:-1] + ')')

    def stroka_nasledovanya(self):
        list = []
        if self.ui.checkBox.isChecked():
            list.append('(F)')
        if self.ui.checkBox_2.isChecked():
            list.append('(OI)')
        if self.ui.checkBox_3.isChecked():
            list.append('(CI)')
        stroka = str(list)
        stroka = stroka.replace('[\'', '').replace('\']', '').replace('\'', '').replace(',', '').replace(' ', '')
        print(stroka)
        return stroka

    def dop_prava(self):
        stroka = ''
        if self.ui.checkBox.isChecked():
            stroka = stroka + '(F),'
        if self.ui.checkBox_2.isChecked():
            stroka = stroka + '(OI),'
        if self.ui.checkBox_3.isChecked():
            stroka = stroka + '(CI),'
        print(stroka[0:-1])
        return stroka



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())