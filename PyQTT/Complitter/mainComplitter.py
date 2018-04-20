import sys
# Импортируем наш интерфейс из файла
from PyQTT.Complitter.guiComplitter import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt
from ldap3 import Server, Connection, SIMPLE, SYNC, ASYNC, SUBTREE, ALL

class MyWin(QtWidgets.QMainWindow):

    spisok = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.LdapGetUsers()
        self.Compliteer()
        self.ui.pushButton.clicked.connect(self.Add)
        self.ui.lineEdit.textEdited.connect(self.ViewPlainText)
        self.ui.lineEdit.returnPressed.connect(self.Add)

    def Add(self):
        text = self.ui.lineEdit.text()
        Localspisok = str(self.spisok)

        if Localspisok.find(text) == -1:
            self.spisok.append(text)
            self.ViewPlainText()
            self.Compliteer()
        return

    def ViewPlainText(self):
        self.ui.plainTextEdit.setPlainText(str(self.spisok))

    def Compliteer(self):
        # Создаём QCompleter, в который устанавливаем список, а также указатель на родителя
        completer = QCompleter(self.spisok, self)
        self.ui.lineEdit.setCompleter(completer)  # Устанавливает QCompleter в поле ввода
        self.ui.gridLayout.addWidget(self.ui.lineEdit, 1, 0, 1, 1)  # Добавляем поле ввода в сетку

    # Получение списка пользователей из ад
    def LdapGetUsers(self):
        AD_SERVER = 'kgndc-01'
        AD_USER = 'dcadmin3@mfckgn.local'
        AD_PASSWORD = "Yjdfz'hf!"
        AD_SEARCH_TREE = 'dc=mfckgn,dc=local'

        server = Server(AD_SERVER)
        conn = Connection(server, user=AD_USER, password=AD_PASSWORD)
        conn.bind()

        conn.search(AD_SEARCH_TREE,
                    '(&(objectCategory=Person)(!(UserAccountControl:1.2.840.113556.1.4.803:=2))(givenName=*)(sn=*))',
                    SUBTREE,
                    attributes=['cn', 'proxyAddresses', 'department', 'sAMAccountName', 'displayName',
                                'telephoneNumber', 'ipPhone', 'streetAddress',
                                'title', 'manager', 'objectGUID', 'company', 'lastLogon']
                    )

        for entry in conn.entries:
            print(entry.sAMAccountName[0]) # внутри списка еще какая то хуйня по этому беру только первый элемент
            self.spisok.append(entry.sAMAccountName[0])





if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())