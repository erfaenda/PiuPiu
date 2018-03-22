import sys
import subprocess
# Импортируем наш интерфейс из файла
from PyQTT.xCacls_shell.iCaclsGUI_2 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton_2.clicked.connect(self.getDcSid)
        self.ui.lineEdit_2.returnPressed.connect(self.getDcSid)
        self.ui.pushButton_4.clicked.connect(self.setAllChekcboxCheck)

    # поиск локальных пользователей на пк
    def getLocalSid(self):
        user = self.ui.lineEdit_2.text()
        cmdline = ['powershell', '$objUser = New-Object System.Security.Principal.NTAccount("{}"); $strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]); $strSID.Value'.format(user)]
        proc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
        out = proc.communicate()
        finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
        print(finalSid)
        proc.wait()
        self.ui.plainTextEdit.appendPlainText(finalSid)

    def getDcSid(self):
        cmdline = ['powershell', '$User = New-Object System.Security.Principal.NTAccount("mfckgn.local", "a.silantev"); $SID = $User.Translate([System.Security.Principal.SecurityIdentifier]); $SID.Value']
        proc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
        out = proc.communicate()
        finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
        proc.wait()
        self.ui.plainTextEdit.appendPlainText(finalSid)

    # отслеживаю нажатие  ентера и выполняю функцию
    def keyPressEvent(self, e):
            if e.key() == QtCore.Qt.Key_Enter:
                self.getSid()

    def setAllChekcboxCheck(self, checked=0):
        for chekboxes in self.ui.buttonGroup.buttons():
            chekboxes.setChecked(checked)

    '''def setAllChekcboxCheck(self, checked=True):
        for chekboxes in self.ui.buttonGroup:
            chekboxes.setChecked(checked)

    def setAllButtonsChecked(self, checked=True):
        for button in self.group.buttons():
            button.setChecked(checked)
            
    def ClearAll(self):
        chekboxes = [self.ui.checkBox.]
        for i in'''

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())