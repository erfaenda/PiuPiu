import sys
# Импортируем наш интерфейс из файла
from PassVAL.guiPassVal import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PassVAL.md5 import *
from PassVAL.Prod.CsvWorker import *
from PyQt5.QtWidgets import QTableWidgetItem

FILENAME = "test_csv.csv"
data = []
# заполнение данными
with open(FILENAME, "r", encoding='utf-8', newline="") as file:
    # читаем файл целиком
    reader = csv.reader(file)
    for row in reader:
        data.append((row[0], row[1], row[2]))
        print(row[0], " - ", row[1], " - ", row[2])
    file.close()

'''data.append(('Заполнить', 'QTableWidget', 'Моя игра'))
data.append(('с данными', 'в Python'))
'''

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
        self.ui.pushButton_2.clicked.connect(self.add_to_csv_table)
        # Кол-во рядов меняется в зависимости от значений в data.
        self.ui.tableWidget.setRowCount(len(data))
        # заголовки
        self.ui.tableWidget.setHorizontalHeaderLabels(("Ресурс", "Логин", "Пароль"))
        # Кол-во столбцов меняется в зависимости от data.
        self.ui.tableWidget.setColumnCount(len(data[0]))
        #Создание объектов классов
        headers = CsvWorker()

        #headers.write_headers() # создаю заголовки в csv
        # заполнение данными

    def fill_table(self):
        # заполнение данными
        with open(FILENAME, "r", encoding='utf-8', newline="") as file:
            # читаем файл целиком
            reader = csv.reader(file)
            for row in reader:
                data.append((row[0], row[1], row[2]))
                print(row[0], " - ", row[1], " - ", row[2])
            file.close()

        row = 0
        for tup in data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1
# при нажатии на кнопку
    def login(self):
        md5 = PasswdManipulation()
        text_in_lable = md5.checkPasswd(self.ui.lineEdit.text())
        self.ui.label.setText(text_in_lable)
    # Добавление значений в csv и заполнение таблицы из csv
    def add_to_csv_table(self):
        woker = CsvWorker()
        ready_data = {"Ресурс:": self.ui.lineEdit_2.text(),
                      "Логин:": self.ui.lineEdit_3.text(),
                      "Пароль:": self.ui.lineEdit_4.text()}
        print(ready_data)
        woker.fill_csv(ready_data)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())