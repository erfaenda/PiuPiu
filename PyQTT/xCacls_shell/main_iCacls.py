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
        self.ui.pushButton_4.clicked.connect(self.clearCheckbox)


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

    def clearCheckbox(self):
        list_checkboxes = [self.ui.checkBox, self.ui.checkBox_2, self.ui.checkBox_3, self.ui.checkBox_4, self.ui.checkBox_5, \
                           self.ui.checkBox_6, self.ui.checkBox_8, self.ui.checkBox_9, self.ui.checkBox_10, self.ui.checkBox_11, \
                           self.ui.checkBox_12, self.ui.checkBox_13, self.ui.checkBox_14, self.ui.checkBox_15, self.ui.checkBox_16, \
                           self.ui.checkBox_17, self.ui.checkBox_18, self.ui.checkBox_19, self.ui.checkBox_20, self.ui.checkBox_21, \
                           self.ui.checkBox_22, self.ui.checkBox_23, self.ui.checkBox_24, self.ui.checkBox_25, self.ui.checkBox_26, \
                           self.ui.checkBox_27, self.ui.checkBox_28, self.ui.checkBox_29, self.ui.checkBox_30]

        for cheboxes in list_checkboxes:
            cheboxes.setChecked(False)


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