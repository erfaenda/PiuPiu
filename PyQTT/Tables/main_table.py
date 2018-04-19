import sys
# Импортируем наш интерфейс из файла
from PyQTT.Tables.gui_table import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget as QTW

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # Выранивание по контенту
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget_2.resizeColumnsToContents()
        # Запрет редактирования
        self.ui.tableWidget_2.setEditTriggers(QTW.NoEditTriggers)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.Editable)


    def Editable(self):
        self.ui.tableWidget_2.setEditTriggers(QTW.AllEditTriggers)
        self.ui.tableWidget_2.setFocus() # видимо выставляет фокус в самую первую свободную клетку


##### Основные функции #####


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())