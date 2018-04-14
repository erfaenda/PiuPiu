import sys, os
import subprocess
# Импортируем наш интерфейс из файла
from PyQTT.xCacls_shell.iCaclsGUI_2 import *
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QCompleter


class MyWin(QtWidgets.QMainWindow):
    complitter_list = []
    finalSid = ''
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # большая группа чекбоксов должна иметь множественный выбор, наследовавние тоже
        self.ui.buttonGroup_3.setExclusive(False)
        self.ui.buttonGroup_2.setExclusive(False)
        self.ui.label_2.setVisible(False)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.action.triggered.connect(self.close)
        self.ui.pushButton_4.clicked.connect(self.clearAllCheckboxes)
        self.ui.buttonGroup_3.buttonClicked.connect(self.clear1Checkboxes)
        self.ui.buttonGroup.buttonClicked.connect(self.clear2Checkboxes)
        self.ui.pushButton.clicked.connect(self.choose_directory)
        self.ui.pushButton_3.clicked.connect(self.main_function)
        self.ui.pushButton_5.clicked.connect(self.access_deny)
        self.ui.pushButton_6.clicked.connect(self.takeown)
        self.ui.pushButton_7.clicked.connect(self.off_nasled)
        self.ui.pushButton_2.clicked.connect(self.check_checkbox)
        self.ui.pushButton_8.clicked.connect(self.check_accsess)
        self.ui.pushButton_9.clicked.connect(self.ui.plainTextEdit.clear)
        self.ui.pushButton_2.clicked.connect(self.dc_or_local)
        self.ui.lineEdit_2.returnPressed.connect(self.dc_or_local)

    # Выбор какую функцию юзать локал или домен
    def dc_or_local(self):
        if self.ui.checkBox_33.isChecked():
            return self.getLocalSid()
        else:self.getDcSid()

    # Комплиттер
    def Compliteer(self):
        # Создаём QCompleter, в который устанавливаем список, а также указатель на родителя
        completer = QCompleter(self.complitter_list, self.ui.lineEdit_2)
        self.ui.lineEdit_2.setCompleter(completer)  # Устанавливает QCompleter в поле ввода
        self.ui.gridLayout.addWidget(self.ui.lineEdit_2, 1, 0, 1, 1)  # Добавляем поле ввода в сетку

    # Функция добавления в комплитер, проверка на дубликаты
    def AddToCompliterList(self):
        text = self.ui.lineEdit_2.text()
        spisok = str(self.complitter_list)
        if spisok.find(text) == -1:
            self.complitter_list.append(text)
        return

    # Проверки
    # Пустой юзер
    def empty_user(self):
        user = self.ui.lineEdit_2.text()
        if len(user) == 0:
            QMessageBox.warning(self, "Ошибка", "Вы не указали пользователя!")
            return
    # Не верный или пустой сид
    def wrongSid(self):
        if len(self.finalSid) > 50:
            QMessageBox.warning(self, "Ошибка", "Пользователь: {} не найден!".format(self.ui.lineEdit_2.text()))
            return
        if self.finalSid == '':
            QMessageBox.warning(self, "Ошибка", "Пользователь: {} не найден!".format(self.ui.lineEdit_2.text()))
            return

    # поиск локальных пользователей на пк
    def getLocalSid(self):
        if self.empty_user():
            return
        cmdline = ['powershell', '$objUser = New-Object System.Security.Principal.NTAccount("{}");'
                                 ' $strSID = $objUser.Translate([System.Security.Principal.SecurityIdentifier]);'
                                 ' $strSID.Value'.format(self.ui.lineEdit_2.text())]
        proc = subprocess.Popen(cmdline, shell=False, stdout=subprocess.PIPE)
        for line in proc.stdout:
            line = line.strip()
            fline = line.decode('cp866')
            self.ui.plainTextEdit.appendPlainText(line.decode('cp866'))
        proc.stdout.close()
        self.finalSid = fline
        #self.finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
        if self.wrongSid():
            return
        self.ui.plainTextEdit.appendPlainText(self.finalSid)
        self.ui.label.setText('{} SID'.format(self.ui.lineEdit_2.text() + ' is: ' + self.finalSid))
        self.AddToCompliterList()
        #self.Compliteer()
        self.check_accsess()

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
        if len(user) == 0:
            QMessageBox.warning(self, "Ошибка", "Вы не указали пользователя!")
            return
        cmdline = ['powershell', '$User = New-Object System.Security.Principal.NTAccount("mfckgn.local", "{}"); $SID = $User.Translate([System.Security.Principal.SecurityIdentifier]); $SID.Value'.format(user)]
        proc = subprocess.Popen(cmdline, shell=True, stdout=subprocess.PIPE)
        out = proc.communicate()
        proc.wait()
        self.finalSid = str(out).rstrip('\\r\\n\', None)').lstrip('(b\'')
        if len(finalSid) > 50:
            QMessageBox.warning(self, "Ошибка", "Пользователь: {} не найден!".format(user))
            return
        #error_string = finalSid.find('Exception')
        #if error_string > -1:
        #    QMessageBox.warning(self, "Ошибка", "Пользователь: {} не найден!".format(user))
        #    return
        if finalSid == '':
            QMessageBox.warning(self, "Ошибка", "Пользователь: {} не найден!".format(user))
            return

        self.ui.plainTextEdit.appendPlainText(finalSid)
        self.ui.label.setText('{} SID'.format(user) + ' is: ' + finalSid)
        self.AddToCompliterList()
        self.Compliteer()
        self.check_accsess()

    # Возврат
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
        if os.path.exists(input_dir):
            proc = subprocess.check_output(['icacls.exe', input_dir], shell=True, stderr=subprocess.STDOUT)
            print(proc.decode('cp866'))
            self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))
        elif input_dir == '':
            QMessageBox.warning(self, "Ошибка", "Не указан путь к папке")
            return
        else:
            QMessageBox.warning(self, "Ошибка", "Путь {} не существует".format(input_dir))
            return

    # формирование строки для дополнительных прав, вида: RC,WA,WEA итд
    def dop_prava(self):
        groupe = self.ui.buttonGroup_3.buttons()
        a = 0
        for checkboxes in groupe:
            if checkboxes.isChecked():
                a = 1
                break
        if a:
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

            stroka = '(' + stroka[0:-1] + ')'
            print(stroka[0:-1])
            return stroka
        return ''

    # формирование строки наследований
    def stroka_nasledovanya(self):
        stroka = ''
        if self.ui.checkBox_21.isChecked():
            stroka = stroka + '(OI)'
        if self.ui.checkBox_22.isChecked():
            stroka = stroka + '(CI)'
        if self.ui.checkBox_23.isChecked():
            stroka = stroka + '(IO)'
        if self.ui.checkBox_24.isChecked():
            stroka = stroka + '(NP)'
        if self.ui.checkBox_25.isChecked():
            stroka = stroka + '(I)'

        return stroka

    # формирование строки основных прав
    def osnovnie_prava(self):
        stroka = ''
        if self.ui.checkBox_26.isChecked():
            stroka = stroka + '(N)'
        if self.ui.checkBox_27.isChecked():
            stroka = stroka + '(F)'
        if self.ui.checkBox_28.isChecked():
            stroka = stroka + '(M)'
        if self.ui.checkBox_29.isChecked():
            stroka = stroka + '(RX)'
        if self.ui.checkBox_31.isChecked():
            stroka = stroka + '(R)'
        if self.ui.checkBox_32.isChecked():
            stroka = stroka + '(W)'
        if self.ui.checkBox_30.isChecked():
            stroka = stroka + '(D)'

        return stroka

    # Проверка чекбоксов
    def check_checkbox(self):
        group = self.ui.buttonGroup.buttons() + self.ui.buttonGroup_2.buttons() + self.ui.buttonGroup_3.buttons()
        for checkbox in group:
            if checkbox.isChecked():
                return True
        return False

    # основная функция раздачи прав
    def main_function(self):
        self.canceled = False
        self.ui.label_2.setVisible(True)
        user = self.ui.lineEdit_2.text()
        if len(user) == 0:
            QMessageBox.warning(self, "Ошибка", "Вы не указали пользователя!")
            return
        if self.check_checkbox() == 0:
            QMessageBox.warning(self, "Ошибка", "Права не выбраны")
            return
        cmdline = ['/grant[:r] *{0}:{1}{2}{3} /T /C'.format(self.finalSid, self.stroka_nasledovanya(), self.osnovnie_prava(), self.dop_prava())]
        if self.finalSid == '':
            QMessageBox.warning(self, "Ошибка", "Незвестное значение, SID не найден!")
            return
        input_dir = self.ui.lineEdit.text()
        if os.path.exists(input_dir):
            proc = subprocess.Popen(['icacls', input_dir, cmdline], shell=True, stdout=subprocess.PIPE)
            self.progress = QtWidgets.QProgressDialog('Пересчет прав', 'Стоп', 0, self.dirs_and_files(), self.ui.lineEdit)
            self.progress.setWindowModality(QtCore.Qt.WindowModal)
            self.progress.setMinimumDuration(10)
            i = -1
            for line in proc.stdout:
                self.progress.setValue(i)
                if self.progress.wasCanceled():
                    self.canceled = True
                    return
                line = line.strip()
                self.ui.plainTextEdit.appendPlainText(line.decode('cp866'))
                i = i + 1
                b = str(i)
                self.ui.label_2.setText(b)
            self.progress.deleteLater()
            self.ui.label_2.setVisible(False)
            proc.stdout.close()
            proc.terminate()
            self.check_accsess()
        elif input_dir == '':
            QMessageBox.warning(self, "Ошибка", "Не указан путь к папке")
            return
        else:
            QMessageBox.warning(self, "Ошибка", "Путь {} не существует".format(input_dir))
            return


    # забираем права
    def access_deny(self):
        user = self.ui.lineEdit_2.text()
        if len(user) == 0:
            QMessageBox.warning(self, "Ошибка", "Вы не указали пользователя!")
            return
        input_dir = self.ui.lineEdit.text()
        if os.path.exists(input_dir):
            cmdline = ['/remove[:g] *{} /T /C'.format(self.finalSid)]
            if self.finalSid == '':
                QMessageBox.warning(self, "Ошибка", "Незвестное значение, SID не найден!")
                return
            proc = subprocess.check_output(['icacls.exe', input_dir, cmdline], shell=True, stderr=subprocess.STDOUT)
            print(cmdline)
            print(proc.decode('cp866'))
            self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))
            self.check_accsess()
        elif input_dir == '':
            QMessageBox.warning(self, "Ошибка", "Не указан путь к папке")
            return
        else:
            QMessageBox.warning(self, "Ошибка", "Путь {} не существует".format(input_dir))
            return
    # стать владельцем
    def takeown(self):
        input_dir = self.ui.lineEdit.text()
        if os.path.exists(input_dir):
            dir = input_dir.replace('/', '\\')
            cmdline = [' /F "{}" /R'.format(dir)]
            proc = subprocess.check_output(['takeown.exe', cmdline], shell=True, stderr=subprocess.STDOUT)
            print(cmdline)
            print(proc.decode('cp866'))
            self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))
        elif input_dir == '':
            QMessageBox.warning(self, "Ошибка", "Не указан путь к папке")
            return
        else:
            QMessageBox.warning(self, "Ошибка", "Путь {} не существует".format(input_dir))
            return
    # отключить наследование I
    def off_nasled(self):
        input_dir = self.ui.lineEdit.text()
        if os.path.exists(input_dir):
            dir = input_dir.replace('\/', '\\')
            cmdline = ['/inheritance:d']
            proc = subprocess.check_output(['icacls.exe', dir, cmdline], shell=True, stderr=subprocess.STDOUT)
            print(cmdline)
            print(proc.decode('cp866'))
            self.ui.plainTextEdit.appendPlainText(proc.decode('cp866'))
            self.check_accsess()
        elif input_dir == '':
            QMessageBox.warning(self, "Ошибка", "Не указан путь к папке")
            return
        else:
            QMessageBox.warning(self, "Ошибка", "Путь {} не существует".format(input_dir))
            return

    # пересчет файлов и папок
    def dirs_and_files(self):
        src = self.ui.lineEdit.text()
        z = 0
        for dir_name, dirs, files in os.walk(src):
            i = 0
            a = i + len(dirs) + len(files)
            z = z + a
        return z

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
