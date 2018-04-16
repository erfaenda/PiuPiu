import sys
# Импортируем наш интерфейс из файла
from PyQTT.Tables.gui_table import *
from PyQt5 import QtCore, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        #self.ui.pushButton_2.clicked.connect(self.choose_directory)



##### Основные функции #####


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())