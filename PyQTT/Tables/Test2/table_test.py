from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

# Импортируем нашу форму.
from PyQTT.Tables.Test2.tableGui import Ui_MainWindow
import sys, csv

FILENAME = "test_csv.csv"

data = []
'''data.append(('Заполнить', 'QTableWidget', 'Моя игра'))
data.append(('с данными', 'в Python'))
'''
with open(FILENAME, "r", encoding='utf-8', newline="") as file:
    #читаем файл целиком
    reader = csv.reader(file)
    for row in reader:
        data.append((row[0], row[1], row[2]))
        #print(row[0], " - ", row[1], " - ", row[2])
    file.close()
    print(data)

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setRowCount(3)
        # action
        self.ui.pushButton.clicked.connect(self.clear)
        # Кол-во рядов меняется в зависимости от значений в data.
        self.ui.tableWidget.setRowCount(len(data))
        # заголовки
        self.ui.tableWidget.setHorizontalHeaderLabels(("Ресурс", "Логин", "Пароль"))
        # Кол-во столбцов меняется в зависимости от data.
        self.ui.tableWidget.setColumnCount(len(data[0]))
        # заполенение
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
    # funck
    def clear(self):
        self.ui.tableWidget.clear()

app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())