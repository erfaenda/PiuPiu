import sys
# Импортируем наш интерфейс из файла
from FTP.FTPQT.gui_ftpqt import *
from ftplib import FTP
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #action
        self.ui.pushButton.clicked.connect(self.connectToFtp)
        #self.ui.listWidget.itemActivated.connect(self.test)
        self.ui.listWidget.itemDoubleClicked.connect(self.move_to_dir)


    currentTextDir = ''

    def connectToFtp(self):
        ftp = FTP('ftp.cse.buffalo.edu')
        ftp.login()  # вошел
        self.ui.listWidget.clear()
        data = ftp.nlst()
        self.ui.listWidget.addItems(data)
        #textdir = self.ui.listWidget.currentItem().text()
        #ftp.cwd(textdir)
        print(data)

    def move_to_dir(self):
        ftp = FTP('ftp.cse.buffalo.edu')
        ftp.login()
        textdir = self.ui.listWidget.currentItem().text()
        ftp.cwd(textdir)
        data = ftp.nlst()
        self.ui.listWidget.addItems(data)
        print(data)



    def test(self):
        print(self.ui.listWidget.currentRow())
        print(self.ui.listWidget.currentItem().text())
        '''if self.ui.listWidget.currentIndex() == 0:
            self.ui.listWidget.
            print('clicked')
        else:
            print('anather')'''



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())