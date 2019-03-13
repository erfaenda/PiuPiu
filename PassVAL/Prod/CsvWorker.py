import csv

FILENAME = "test_csv.csv"

#Все действия связанные с CSV чтение, запись, редактирование
class CsvWorker():
    # запись заголовка
    def write_headers(self):
        with open(FILENAME, "w", encoding='utf-8', newline="") as file:
            columns = ['Ресурс:', 'Логин:', 'Пароль:']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            file.close()

    ready_data = {"Ресурс:": "вк", "Логин:": "петя", "Пароль:": "супер пароль"}

    # заполнение полей словарем по ключам заголовков
    def fill_csv(self, ready_data):
        with open(FILENAME, "a", encoding='utf-8', newline="") as file:
            columns = ['Ресурс:', 'Логин:', 'Пароль:']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow(ready_data)
            file.close()

    # чтение файла целиком по строчно
    def read_csv(self):
        with open(FILENAME, "r", encoding='utf-8', newline="") as file:
            #читаем файл целиком
            reader = csv.reader(file)
            data_in_csv = []
            for row in reader:
                print(row[0], " - ", row[1], " - ", row[2])
                data_in_csv.append((row[0], row[1], row[2]))
                #data = row[0], row[1], row[2]
                return data_in_csv
            file.close()

    # Заполнение виджета таблицы из массива полученного с csv
    def fill_table(self, FILENAME, QTableWidgetItem, tableWidget, data):
        # чтение из csv и добавление в массив
        with open(FILENAME, "r", encoding='utf-8', newline="") as file:
            # читаем файл целиком
            reader = csv.reader(file)
            for row in reader:
                data.append((row[0], row[1], row[2]))
                print(row[0], " - ", row[1], " - ", row[2])
            file.close()
        # заполенине виджета таблицы данными
        row = 0
        for tup in data:
            col = 0
            for item in tup:
                cellinfo = QTableWidgetItem(item)
                tableWidget.setItem(row, col, cellinfo)
                col += 1
            row += 1

if __name__ == "__main__":
    app = CsvWorker
    app.read_csv()