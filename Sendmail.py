import smtplib, MySQLdb, time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Давно уже не программировал, заранее извиняюсь за быдло-код.
class WorkerProcess():
    # Глобальные переменные
    MESSAGE = ''
    TRIGGER = 1
    def ReadMySQL(self):
        handle = open("memoris.ini", "r")
        lastuser = int(handle.readline())
        print('Последнее число в файле ',lastuser)# читаю первую строку
        handle.close()
        # Открыть соединение с базой данных
        db = MySQLdb.connect("10.9.155.12", "ADAdmin2", "Ktcjecnhjqcndj2019", "ADAdmin", charset="utf8")
        # Подготовка объекта cursor с помощью метода cursor()
        cursor = db.cursor()
        # Выполнил SQL-запрос с помощью метода execute()
        cursor.execute("SELECT * FROM loglist WHERE ID = (SELECT MAX(ID) FROM loglist)")
        # Получить одну строку с помощью метода fetchone()
        data = cursor.fetchone()
        if lastuser < data[0]:
            lastuser = str(data[0])
            print('Был добавлен пользователь:', data[4], data[5], data[6], data[13])
            self.MESSAGE = (data[4] + ' ' + data[5] + ' ' + data[6] + ' ' + data[13]) # Так пишет человек который забыл про format^)
            #lastuser = str(lastuser)
            handle = open("memoris.ini", "w")
            handle.write(lastuser)
            handle.close()
            self.TRIGGER = 1
        else:
            self.TRIGGER = 0
        # отключение от сервера
        db.close()

    def Sendemail(self):
        fromaddr = "a.silantev@mfc45.ru"
        mypass = "a011787b"
        toaddr = ["m.petrov@mfc45.ru", "a.silantev@mfc45.ru"]
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = ', '.join(toaddr)
        msg['Subject'] = "Уведомление о добавлении нового пользователя!"
        body = self.MESSAGE
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('mail.mfc45.ru', 587)
        server.starttls()
        server.login(fromaddr, mypass)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

if __name__=="__main__":
    myapp = WorkerProcess()
    while True:
        myapp.ReadMySQL()
        if myapp.TRIGGER == 1:
            myapp.Sendemail()
        else:
            print('Ничего не зименилось')
        time.sleep(1200)

