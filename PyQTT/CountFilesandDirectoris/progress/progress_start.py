import sys, os
# Импортируем наш интерфейс из файла
from PyQTT.CountFilesandDirectoris.progress.progress_gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton_2.clicked.connect(self.choose_directory)
        self.ui.pushButton.clicked.connect(self.dirs_and_files)


##### Основные функции #####
    # диалог выбора файла или папки
    def choose_directory(self):
        input_dir = QFileDialog.getExistingDirectory(None, 'Выберете директорию: ')
        if os.path.exists(input_dir):
            self.ui.lineEdit.setText(input_dir)
        return

    # програмирование ради програмирования
    # считаем количество файлов что бы потом запустить прогресс бар в подсчете количества файлов =)
    def just_progz(self):
        src = self.ui.lineEdit.text()
        z = 0
        for dir_name, dirs, files in os.walk(src):
            i = 0
            a = i + len(dirs) + len(files)
            z = z + a
        return z

    # Пересчет количства файлов и папок
    def dirs_and_files(self):
        src = self.ui.lineEdit.text()
        z = 0
        self.progress = QtWidgets.QProgressDialog('Поиск....', 'Стоп', 0, self.just_progz(), self.ui.lineEdit)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.setMinimumDuration(10)
        for dir_name, dirs, files in os.walk(src):
            self.progress.setValue(z)
            i = 0
            a = i + len(dirs) + len(files)
            z = z + a
            f = str(z)
            self.ui.label.setText(f)
        self.progress.deleteLater()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())