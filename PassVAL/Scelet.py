import sys
# Импортируем наш интерфейс из файла
from PassVAL.guiPassVal import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PassVAL.md5 import *
from PassVAL.Prod.CsvWorker import *
from PyQt5.QtWidgets import QTableWidgetItem
from PassVAL.Child_1 import *
from PassVAL.Encrypt import *

FILENAME = "test_csv.csv"
data = []
# заполнение массива данными из файла csv для создания пустых строк таблицы
with open(FILENAME, "r", encoding='utf-8', newline="") as file:
    # читаем файл целиком
    reader = csv.reader(file)
    for row in reader:
        data.append((row[0], row[1], row[2]))
    file.close()

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # иконы купола
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('ic.ico'))
        self.ui.statusbar.showMessage('© Alexey Silantyev, 2019')
        # ---- BUTTONS BLOCK ----- Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.lineEdit.returnPressed.connect(self.login)
        self.ui.pushButton_2.clicked.connect(self.add_to_csv_table)
        self.ui.pushButton_3.clicked.connect(self.add_empty_table_field)
        self.ui.pushButton_4.clicked.connect(self.save_data_in_csv)
        self.ui.exit.triggered.connect(self.close)
        self.ui.change_password.triggered.connect(self.open_change_password_dialog)
        # -------------------------------------------------------
        # Кол-во рядов меняется в зависимости от значений в data.
        self.ui.tableWidget.setRowCount(len(data))
        # заголовки
        self.ui.tableWidget.setHorizontalHeaderLabels(("Ресурс", "Логин", "Пароль"))
        # Кол-во столбцов меняется в зависимости от data.
        self.ui.tableWidget.setColumnCount(len(data[0]))

    # сравнивание мд5 суммы мастер ключа с фактический введенным паролем
    def login(self):
        md5 = PasswdManipulation()
        logon = md5.checkPasswd(self.ui.lineEdit.text())
        if logon is True:
            self.ui.label.setText('Пароль верный')
            # заполнение данными
            self.fill_table_with_csv()
        else:
            self.ui.label.setText('Пароль не существует')
    # добавление пустой строки в таблицу
    def add_empty_table_field(self):
        last_row = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(last_row)
        print(last_row)

    # добавление данных из таблицы в csv базу
    def save_data_in_csv(self):
        #data = []
        encript = Encription()
        with open(FILENAME, "w", encoding='utf-8', newline="") as file:
            columns = ['Ресурс:', 'Логин:', 'Пароль:']
            writer = csv.DictWriter(file, fieldnames=columns)

            for r in range(0, self.ui.tableWidget.rowCount()):
                row_list = []
                for c in range(0, self.ui.tableWidget.columnCount()):
                    text = self.ui.tableWidget.item(r, c).text()
                    encript_text = encript.encrypt_trans(text)
                    #row_list.append(self.ui.tableWidget.item(r, 2).text())
                    row_list.append(encript_text)
                string_table = dict(zip(['Ресурс:', 'Логин:', 'Пароль:'], row_list))
                writer.writerow(string_table)

    # заполнение таблицы из csv базы
    def fill_table_with_csv(self):
        encript = Encription()
        row = 0
        for tup in data:
            #print(tup)
            col = 0
            for item in tup:
                #cellinfo = QTableWidgetItem(encript.decrypt(item))
                cellinfo = QTableWidgetItem(item)
                #cellinfob = QTableWidgetItem(bytes(item, 'utf8'))

                print(bytes(item, 'utf8'))
                print(encript.decrypt(bytes(item, 'utf8')))
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

    # Добавление значений в csv и заполнение таблицы из csv
    def add_to_csv_table(self):
        woker = CsvWorker()
        ready_data = {"Ресурс:": self.ui.lineEdit_2.text(),
                      "Логин:": self.ui.lineEdit_3.text(),
                      "Пароль:": self.ui.lineEdit_4.text()}
        print(ready_data)
        woker.fill_csv(ready_data)

    # --------------- Дочерние окна -------------------
    # Открытие окна диалога смены мастер пароля
    def open_change_password_dialog(self):
        # child_window.ui.lineEdit.setText(self.ui.label_10.text())
        change_password_dialog_window_1.show()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    change_password_dialog_window_1 = Child_1()
    myapp.show()
    sys.exit(app.exec_())