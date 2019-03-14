import csv


def csv_dict_reader(file):
    """
    Read a CSV file using csv.DictReader
    """
    reader = csv.DictReader(file, delimiter=',')
    for line in reader:
        print(line["Ресурс:"])
        print(line["nick"])
        print(line["age"])

if __name__ == "__main__":
    with open("test_csv.csv") as file:
        csv_dict_reader(file)