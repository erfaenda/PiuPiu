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
        self.ui.pushButton_2.clicked.connect(self.getSid)
        self.ui.lineEdit_2.returnPressed.connect(self.getSid)

    def getSid(self):
        user = self.ui.lineEdit_2.text()
        proc = subprocess.Popen(
            ['powershell', '$objUser = New-Object System.Security.Principal.NTAccount(\"' + user + '\"); '
                                                                                                   '$strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]); $strSID.Value'],
            shell=True, stdout=subprocess.PIPE)
        out = proc.communicate()
        finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
        print(finalSid)
        proc.wait()
        self.ui.plainTextEdit.appendPlainText(finalSid)

    # отслеживаю нажатие  ентера и выполняю функцию
    def keyPressEvent(self, e):
            if e.key() == QtCore.Qt.Key_Enter:
                self.getSid()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())