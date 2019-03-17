import sys

from PassVAL.guiChild_1 import *
from PassVAL.md5 import *
from PyQt5 import QtWidgets

class Child_1(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Child_1()
        self.ui.setupUi(self)
        # slots
        self.ui.pushButton_2.clicked.connect(self.check_old_password)
        self.ui.lineEdit.returnPressed.connect(self.check_old_password)
        self.ui.lineEdit_2.returnPressed.connect(self.new_master_password_md5)

    def check_old_password(self):
        md5 = PasswdManipulation()
        logon = md5.checkPasswd(self.ui.lineEdit.text())
        if self.ui.lineEdit_2.isEnabled():
            self.new_master_password_md5()
        else:
            if logon is True:
                self.ui.lineEdit.setText('')
                self.ui.label.setText('Введите новый пароль_________')
                self.ui.lineEdit_2.setEnabled(True)
                print('da')
                self.ui.pushButton_2.clicked.connect(self.new_master_password_md5)
            else:
                self.ui.label.setText('Пароль не верный')
                print('no')

    def new_master_password_md5(self):
        if self.ui.lineEdit.text() == self.ui.lineEdit_2.text():
            print('Совпадают пароли')
            md5 = PasswdManipulation()
            md5.makeThisShit(self.ui.lineEdit.text())
            self.ui.label.setText('Новый пароль принят')
        else:
            print('не совпадают пароли')
            self.ui.label.setText('Пароли не совпадают')


