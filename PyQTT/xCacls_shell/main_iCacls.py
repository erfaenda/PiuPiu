import sys
import subprocess
# Импортируем наш интерфейс из файла
from PyQTT.xCacls_shell.iCaclsGUI_2 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # большая группа чекбоксов должна иметь множественный выбор
        self.ui.buttonGroup_3.setExclusive(False)
        self.ui.buttonGroup_2.setExclusive(False)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton_2.clicked.connect(self.getDcSid)
        self.ui.lineEdit_2.returnPressed.connect(self.getDcSid)
        self.ui.pushButton_4.clicked.connect(self.clearAllCheckboxes)
        self.ui.buttonGroup_3.buttonClicked.connect(self.clear1Checkboxes)
        self.ui.buttonGroup.buttonClicked.connect(self.clear2Checkboxes)
        self.ui.pushButton.clicked.connect(self.choose_directory)
        self.ui.pushButton_3.clicked.connect(self.main_function)
        self.ui.pushButton_5.clicked.connect(self.access_deny)
        self.ui.pushButton_6.clicked.connect(self.takeown)
        self.ui.pushButton_7.clicked.connect(self.off_nasled)

    # поиск локальных пользователей на пк
    def getLocalSid(self):
        user = self.ui.lineEdit_2.text()
        if len(user) > 0:
            cmdline = ['powershell', '$objUser = New-Object System.Security.Principal.NTAccount("{}"); $strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]); $strSID.Value'.format(user)]
            proc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
            out = proc.communicate()
            finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
            print(finalSid)
            proc.wait()
            self.ui.plainTextEdit.appendPlainText(finalSid)
            self.ui.label.setText('{} SID'.format(user) + ' is: ' + finalSid)
        else:
            QMessageBox.warning(self, "Ошибка", "Вы не указали пользователя или группу")

    def returnFinalSid(self):
        user = self.ui.lineEdit_2.text()
        cmdline = ['powershell', '$objUser = New-Object System.Security.Principal.NTAccount("{}"); $strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]); $strSID.Value'.format(user)]
        proc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
        out = proc.communicate()
        finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
        proc.wait()
        return finalSid

    # поиск доменного пользовател
    def getDcSid(self):
        user = self.ui.lineEdit_2.text()
        if len(user) > 0:
            cmdline = ['powershell', '$User = New-Object System.Security.Principal.NTAccount("mfckgn.local", "{}"); $SID = $User.Translate([System.Security.Principal.SecurityIdentifier]); $SID.Value'.format(user)]
            proc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
            out = proc.communicate()
            finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
            if finalSid == '':
                QMessageBox.warning(self, "Ошибка", "Пользователь: {} не найден!".format(user))
            else:
                proc.wait()
                self.ui.plainTextEdit.appendPlainText(finalSid)
                self.ui.label.setText('{} SID'.format(user) + ' is: ' + finalSid)
                self.check_accsess()
        else:
            QMessageBox.warning(self, "Ошибка", "Вы не указали пользователя или группу")

    def returnDcSid(self):
        user = self.ui.lineEdit_2.text()
        cmdline = ['powershell', '$User = New-Object System.Security.Principal.NTAccount("mfckgn.local", "{}"); $SID = $User.Translate([System.Security.Principal.SecurityIdentifier]); $SID.Value'.format(user)]
        proc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
        out = proc.communicate()
        finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
        proc.wait()
        return finalSid

    # отслеживаю нажатие  ентера и выполняю функцию
    def keyPressEvent(self, e):
            if e.key() == QtCore.Qt.Key_Enter:
                self.getSid()

    # Первое что пришло в голову
    '''def clearCheckbox(self):
        list_checkboxes = [self.ui.checkBox, self.ui.checkBox_2, self.ui.checkBox_3, self.ui.checkBox_4, self.ui.checkBox_5, \
                           self.ui.checkBox_6, self.ui.checkBox_8, self.ui.checkBox_9, self.ui.checkBox_10, self.ui.checkBox_11, \
                           self.ui.checkBox_12, self.ui.checkBox_13, self.ui.checkBox_14, self.ui.checkBox_15, self.ui.checkBox_16, \
                           self.ui.checkBox_17, self.ui.checkBox_18, self.ui.checkBox_19, self.ui.checkBox_20, self.ui.checkBox_21, \
                           self.ui.checkBox_22, self.ui.checkBox_23, self.ui.checkBox_24, self.ui.checkBox_25, self.ui.checkBox_26, \
                           self.ui.checkBox_27, self.ui.checkBox_28, self.ui.checkBox_29, self.ui.checkBox_30, self.ui.checkBox_31, \
                           self.ui.checkBox_32, self.ui.checkBox_7]

        for cheboxes in list_checkboxes:
            cheboxes.setChecked(False)'''

    # второе что пришло в голову, кастыль
    '''def setAllChekcboxCheck(self):
        for chekboxes in self.ui.buttonGroup.buttons():
            if chekboxes.checkState() == Qt.Checked:
                chekboxes.setCheckable(False)
            else:
                chekboxes.setCheckable(True)'''

    # так поидее должно было работать но не работает
    '''def radioClear(self):
        list = [self.ui.checkBox_26, self.ui.checkBox_27, self.ui.checkBox_28]
        for i in list:
            i.setCheckable(False)
            i.setCheckable(True)'''

    # снятие чекбоксов во всехблоках
    def clearAllCheckboxes(self):
        groups = self.ui.buttonGroup.buttons() + self.ui.buttonGroup_2.buttons() + self.ui.buttonGroup_3.buttons()
        self.ui.buttonGroup.setExclusive(False) #снимает эффект радиобатона, в этот момент можно работать как с обычным чекбоксом
        self.ui.buttonGroup_2.setExclusive(False)
        self.ui.buttonGroup_3.setExclusive(False)
        for button in groups:
            button.setChecked(False)

        self.ui.buttonGroup.setExclusive(True)


    # очистка первого блока с чекбоксами
    def clear1Checkboxes(self):
        groups = self.ui.buttonGroup.buttons()
        self.ui.buttonGroup.setExclusive(False)
        for button in groups:
            button.setChecked(False)

        self.ui.buttonGroup.setExclusive(True)

    # отчистка второго блока с чекбоксами
    def clear2Checkboxes(self):
        groups = self.ui.buttonGroup_3.buttons()
        self.ui.buttonGroup_3.setExclusive(False)
        for button in groups:
            button.setChecked(False)

    # диалог выбора файла или папки
    def choose_directory(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Выберете директорию: ')
        self.ui.lineEdit.setText(input_dir)
        self.check_accsess()

    # порверка прав доступа на папку
    def check_accsess(self):
        input_dir = self.ui.lineEdit.text()
        proc = subprocess.check_output(['icacls.exe', input_dir], shell=True, stderr=subprocess.STDOUT)
        print(proc.decode('cp866'))
        self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))

    # формирование строки для дополнительных прав, вида: RC,WA,WEA итд
    def dop_prava(self):
        stroka = ''
        if self.ui.checkBox.isChecked():
            stroka = stroka + 'DE,'
        if self.ui.checkBox_2.isChecked():
            stroka = stroka + 'RC,'
        if self.ui.checkBox_3.isChecked():
            stroka = stroka + 'WDAC,'
        if self.ui.checkBox_4.isChecked():
            stroka = stroka + 'WO,'
        if self.ui.checkBox_5.isChecked():
            stroka = stroka + 'S,'
        if self.ui.checkBox_6.isChecked():
            stroka = stroka + 'AS,'
        if self.ui.checkBox_7.isChecked():
            stroka = stroka + 'MA,'
        if self.ui.checkBox_8.isChecked():
            stroka = stroka + 'GR,'
        if self.ui.checkBox_9.isChecked():
            stroka = stroka + 'GW,'
        if self.ui.checkBox_10.isChecked():
            stroka = stroka + 'GE,'
        if self.ui.checkBox_19.isChecked():
            stroka = stroka + 'GA,'
        if self.ui.checkBox_15.isChecked():
            stroka = stroka + 'RD,'
        if self.ui.checkBox_18.isChecked():
            stroka = stroka + 'WD,'
        if self.ui.checkBox_13.isChecked():
            stroka = stroka + 'AD,'
        if self.ui.checkBox_16.isChecked():
            stroka = stroka + 'REA,'
        if self.ui.checkBox_17.isChecked():
            stroka = stroka + 'WEA,'
        if self.ui.checkBox_14.isChecked():
            stroka = stroka + 'X,'
        if self.ui.checkBox_12.isChecked():
            stroka = stroka + 'DC,'
        if self.ui.checkBox_20.isChecked():
            stroka = stroka + 'RA,'
        if self.ui.checkBox_11.isChecked():
            stroka = stroka + 'WA,'

        print(stroka[0:-1])
        return stroka
    # формирование строки наследований
    def stroka_nasledovanya(self):
        list = []
        if self.ui.checkBox_21.isChecked():
            list.append('(OI)')
        if self.ui.checkBox_22.isChecked():
            list.append('(CI)')
        if self.ui.checkBox_23.isChecked():
            list.append('(IO)')
        if self.ui.checkBox_24.isChecked():
            list.append('(NP)')
        if self.ui.checkBox_25.isChecked():
            list.append('(I)')
        stroka = str(list)
        stroka = stroka.replace('[\'', '').replace('\']', '').replace('\'', '').replace(',', '').replace(' ', '')
        return stroka

    # формирование строки основных прав
    def osnovnie_prava(self):
        list = []
        if self.ui.checkBox_26.isChecked():
            list.append('(N)')
        if self.ui.checkBox_27.isChecked():
            list.append('(F)')
        if self.ui.checkBox_28.isChecked():
            list.append('(M)')
        if self.ui.checkBox_29.isChecked():
            list.append('(RX)')
        if self.ui.checkBox_31.isChecked():
            list.append('(R)')
        if self.ui.checkBox_32.isChecked():
            list.append('(W)')
        if self.ui.checkBox_30.isChecked():
            list.append('(D)')

        stroka = str(list)
        stroka = stroka.replace('[\'', '').replace('\']', '').replace('\'', '').replace(',', '').replace(' ', '')
        return stroka

    # основная функция раздачи прав
    def main_function(self):
        user = self.ui.lineEdit_2.text()
        if len(user) > 0:
            input_dir = self.ui.lineEdit.text()
            cmdline = ['/grant[:r] *{0}:{1}{2}{3} /T /C'.format(self.returnDcSid(), self.stroka_nasledovanya(), self.osnovnie_prava(), self.dop_prava())]
            if self.returnDcSid() == '':
                QMessageBox.warning(self, "Ошибка", "Незвестное значение, SID не найден!")
            else:
                proc = subprocess.check_output(['icacls.exe', input_dir, cmdline], shell=True, stderr=subprocess.STDOUT)
                print(cmdline)
                print(proc.decode('cp866'))
                self.check_accsess()
        else:
            QMessageBox.warning(self, "Ошибка", "Пользователь {}, не найден!".format(user))

    # забираем права
    def access_deny(self):
        input_dir = self.ui.lineEdit.text()
        cmdline = ['/remove[:g] *{} /T /C'.format(self.returnDcSid())]
        proc = subprocess.check_output(['icacls.exe', input_dir, cmdline], shell=True, stderr=subprocess.STDOUT)
        print(cmdline)
        print(proc.decode('cp866'))
        self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))
        self.check_accsess()

    # стать владельцем
    def takeown(self):
        input_dir = self.ui.lineEdit.text()
        dir = input_dir.replace('/', '\\')
        cmdline = [' /F "{}" /R'.format(dir)]
        proc = subprocess.check_output(['takeown.exe', cmdline], shell=True, stderr=subprocess.STDOUT)
        print(cmdline)
        print(proc.decode('cp866'))
        self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))

    # отключить наследование I
    def off_nasled(self):
        input_dir = self.ui.lineEdit.text()
        dir = input_dir.replace('\/', '\\')
        cmdline = ['/inheritance:d']
        proc = subprocess.check_output(['icacls.exe', dir, cmdline], shell=True, stderr=subprocess.STDOUT)
        print(cmdline)
        print(proc.decode('cp866'))
        self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))
        self.check_accsess()

    # лишняя проверка ненужна если есть слоты
    '''def uncheckRadio(self):
        bigGroupe = self.ui.buttonGroup_3.buttons()
        for checkbox in bigGroupe:
            if checkbox.isChecked():
                self.clear1Checkboxes()'''

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
