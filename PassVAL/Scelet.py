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
# заполнение массива данными из файла csv
with open(FILENAME, "r", encoding='utf-8', newline="") as file:
    # читаем файл целиком
    reader = csv.reader(file)
    for row in reader:
        data.append((row[0], row[1], row[2]))
        #print(row[0], " - ", row[1], " - ", row[2])
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
        self.ui.pushButton_3.clicked.connect(self.add_empty_table_field)
        self.ui.pushButton_4.clicked.connect(self.save_data_in_csv)
        # Кол-во рядов меняется в зависимости от значений в data.
        #self.ui.tableWidget.setRowCount(len(data))
        # заголовки
        self.ui.tableWidget.setHorizontalHeaderLabels(("Ресурс", "Логин", "Пароль"))
        # Кол-во столбцов меняется в зависимости от data.
        #self.ui.tableWidget.setColumnCount(len(data[0]))
        #Создание объектов классов
        csvworker = CsvWorker()
        #self.update_table()
        #headers.write_headers() # создаю заголовки в csv
        # заполнение данными
        self.test_fill()
        '''row = 0
        for tup in data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1'''

    def update_table(self):
        woker = CsvWorker()
        woker.fill_table(FILENAME, QTableWidgetItem, self.ui.tableWidget, data)

    # сравнивание мд5 суммы мастер ключа с фактический введенным паролем
    def login(self):
        md5 = PasswdManipulation()
        text_in_lable = md5.checkPasswd(self.ui.lineEdit.text())
        self.ui.label.setText(text_in_lable)
    # добавление пустой строки в таблицу
    def add_empty_table_field(self):
        last_row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(last_row)
        print(last_row)
    # добавление данных из таблицы в csv базу
    def save_data_in_csv(self):
        data_string = []
        with open(FILENAME, "a", encoding='utf-8', newline="") as file:
            columns = ['Ресурс:', 'Логин:', 'Пароль:']
            writer = csv.DictWriter(file, fieldnames=columns)
            for i in range(self.ui.tableWidget.rowCount()):
                for a in range(self.ui.tableWidget.columnCount()):
                    t = self.ui.tableWidget.item(i, a).text()
                    print(t)
                    data_string.append(t)
                    #writer.writerow({"Ресурс:": self.ui.tableWidget.item(i, a).text(), "Логин:": self.ui.tableWidget.item(i, a).text(), "Пароль:": "супер пароль"})
            writer.writerow({"Ресурс:": data_string[0], "Логин:": data_string[1], "Пароль:": data_string[2]})
            file.close()
    # заполнение таблицы из csv базы
    def test_fill(self):
        data_string = []
        self.ui.tableWidget.setRowCount(len(data))
        self.ui.tableWidget.setColumnCount(len(data[0]))
        with open(FILENAME, "r", encoding='utf-8', newline="") as file:
            reader = csv.reader(file)
            for i in reader:
                #data_string.append((i[0], i[1], i[2]))
                self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(i[0]))
                self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(i[1]))
                self.ui.tableWidget.setItem(0, 2, QTableWidgetItem(i[2]))

                print(data_string)
                #writer.writerow({"Ресурс:": self.ui.tableWidget.item(i, a).text(), "Логин:": self.ui.tableWidget.item(i, a).text(), "Пароль:": "супер пароль"})
            #writer.writerow({"Ресурс:": data_string[0], "Логин:": data_string[1], "Пароль:": data_string[2]})
            #file.close()
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