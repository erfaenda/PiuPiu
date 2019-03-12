import sys
# Импортируем наш интерфейс из файла
from PassVAL.guiPassVal import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PassVAL.md5 import *
from PassVAL.Prod.CsvWorker import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # иконы купола
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('ic.ico'))
        self.ui.statusbar.showMessage('© Alexey Silantyev, 2019')
        # Здесь прописываем событие нажатия на кнопку
        #self.ui.actionExit.triggered.connect(self.close)
        self.ui.pushButton.clicked.connect(self.login)

# при нажатии на кнопку
    def login(self):
        md5 = PasswdManipulation()
        text_in_lable = md5.checkPasswd(self.ui.lineEdit.text())
        self.ui.label.setText(text_in_lable)

    def add_to_table(self):
        woker = CsvWorker()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())