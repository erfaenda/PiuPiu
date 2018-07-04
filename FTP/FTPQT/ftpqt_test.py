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

        #ftp.cwd('bin')
        data = ftp.retrlines('LIST')
        data2 = str(data)
        self.ui.plainTextEdit.appendPlainText(data2)
        print(data2)



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())