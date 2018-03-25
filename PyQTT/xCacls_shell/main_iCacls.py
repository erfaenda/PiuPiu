import sys
import subprocess
# Импортируем наш интерфейс из файла
from PyQTT.xCacls_shell.iCaclsGUI_2 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
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
        self.ui.pushButton_2.clicked.connect(self.getLocalSid)
        self.ui.lineEdit_2.returnPressed.connect(self.getLocalSid)
        self.ui.pushButton_4.clicked.connect(self.clearAllCheckboxes)
        self.ui.buttonGroup_3.buttonClicked.connect(self.clear1Checkboxes)
        self.ui.buttonGroup.buttonClicked.connect(self.clear2Checkboxes)
        self.ui.pushButton.clicked.connect(self.choose_directory)
        self.ui.pushButton_3.clicked.connect(self.main_function)


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
        self.ui.label.setText('{} SID'.format(user) + ' is: ' + finalSid)

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
        proc = subprocess.check_output(['icacls.exe', input_dir], stderr=subprocess.STDOUT)
        print(proc.decode('cp866'))
        self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))

    def list_line(self):
        list = []
        if self.ui.checkBox_27.sta():
            list.append('(F)')
        if self.ui.checkBox_21.isChecked():
            list.append('(OI)')
        if self.ui.checkBox_22.isChecked():
            list.append('(CI)')
        return str(list)

    def main_function(self):
        input_dir = self.ui.lineEdit.text()
        cmdline = ['/grant[:r] *{}:{} /T /C'.format(self.returnFinalSid(), self.list_line())]
        proc = subprocess.check_output(['icacls.exe', input_dir, cmdline], stderr=subprocess.STDOUT)
        print(proc.decode('cp866'))

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