import csv

FILENAME = "test_csv.csv"

def writeHeaders():
    with open(FILENAME, "w", encoding='utf-8', newline="") as file:
        columns = ['Ресурс:', 'Логин:', 'Пароль:']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        file.close()

#writeHeaders()

ready_data = {"Ресурс:": "вк", "Логин:": "петя", "Пароль:": "супер пароль"}

with open(FILENAME, "a", encoding='utf-8', newline="") as file:
    columns = ['Ресурс:', 'Логин:', 'Пароль:']
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writerow(ready_data)
    file.close()

with open(FILENAME, "r", encoding='utf-8', newline="") as file:
    #читаем файл целиком
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1], " - ", row[2])
    file.close()