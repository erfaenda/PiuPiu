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
    def fill_csv(self):
        with open(FILENAME, "a", encoding='utf-8', newline="") as file:
            columns = ['Ресурс:', 'Логин:', 'Пароль:']
            writer = csv.DictWriter(file, fieldnames=columns)
            writer.writerow(self.ready_data)
            file.close()
    # чтение файла целиком по строчно

    def read_csv(self):
        with open(FILENAME, "r", encoding='utf-8', newline="") as file:
            #читаем файл целиком
            reader = csv.reader(file)
            for row in reader:
                print(row[0], " - ", row[1], " - ", row[2])
                data = row[0], row[1], row[2]
                return data
            file.close()