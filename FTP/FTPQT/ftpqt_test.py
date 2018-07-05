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


    def connectToFtp(self):
        ftp = FTP('ftp.cse.buffalo.edu')
        ftp.login()  # вошел
        data = ftp.nlst()

        #ftp.cwd('bin')
        #data = ftp.retrlines('NLST')
        #stri = ['kuka']
        '''for dirs in data:
            fstr = stri.append(dirs)
        print(fstr)'''
        self.ui.listWidget.addItems(data)
        print(data)



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())