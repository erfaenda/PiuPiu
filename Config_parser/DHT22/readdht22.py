import configparser, time

def read_data_DHT22(path):
    while True:
        """
        read, update, delete config
        """

        config = configparser.ConfigParser()
        config.read(path)

        # Читаем некоторые значения из конфиг. файла.
        t = config.get("DHT22_last", "temperature")
        h = config.get("DHT22_last", "humi")

        print("Температура " + t)
        print("Влажность " + h)
        time.sleep(2)

if __name__ == "__main__":
    path = "DHT22.ini"
    read_data_DHT22(path)