import sys, time
# Импортируем наш интерфейс из файла
from PyQTT.GuessWord.gwGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.comboBox.addItems('4 5'.split())
        self.ui.statusbar.showMessage('© Alexey Silantyev, 2018')

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.start1)
        self.ui.pushButton_2.clicked.connect(self.clearText)
        self.ui.lineEdit.returnPressed.connect(self.start1)
        self.ui.action_2.triggered.connect(self.close)

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Подтверждение", "Хотите выйти?",
                                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                    QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
          e.accept()
        else:
          e.ignore()

    # мои функции
    def start1(self):
        if self.ui.comboBox.currentIndex() == 0:
            self.wordFour(self.ui.lineEdit.text())
        elif self.ui.comboBox.currentIndex() == 1:
            self.wordFive(self.ui.lineEdit.text())

    def wordFour(self, letters):
        self.canceled = False
        self.t1 = time.time()
        self.c = 0
        self.resArr = []
        self.initW = letters
        self.res = ["", "", "", ""]
        self.r = open("word_rus.txt", 'r', encoding='utf-8')
        self.fileRead = self.r.read()
        #self.fileSplit = self.fileRead.split()
        # улучшеная версия, ищщет только среди слов в 4 символа
        self.fileSplit0 = self.fileRead.split()
        self.fileSplit = []
        for word in self.fileSplit0:
            if len(word) == 4:
                self.fileSplit.append(word)

        self.r.close()
        self.progress = QtWidgets.QProgressDialog('Поиск....', 'Стоп', 0, len(self.initW), self.ui.lineEdit)
        self.progress.setWindowModality(QtCore.Qt.WindowModal)
        self.progress.setMinimumDuration(100)
        for self.i in range(0, len(self.initW)):
            self.res[0] = self.initW[self.i]
            #индикатор
            self.progress.setValue(self.i)
            if self.progress.wasCanceled():
                self.canceled = True
                return
            for self.q in range(0, len(self.initW)):
                if (self.q != self.i):
                    self.res[1] = self.initW[self.q]
                    for self.p in range(0, len(self.initW)):
                        if (self.p != self.i) and (self.p != self.q):
                            self.res[2] = self.initW[self.p]
                            for self.pp in range(0, len(self.initW)):
                                if (self.pp != self.i) and (self.pp != self.q) and (self.pp != self.p):
                                    self.res[3] = self.initW[self.pp]
                                    self.wordFor = self.res[0] + self.res[1] + self.res[2] + self.res[3]
                                    if self.wordFor in self.fileSplit:
                                        if self.wordFor not in self.resArr:
                                            self.resArr.append(self.wordFor)
                                            self.c += 1
                                            self.str = "Найдено совпадений: " + str(len(self.resArr)) + "\n" + self.arrOutput(self.resArr) + "\n" + str(self.c) + " комбинаций проверено\nВремя исполнения: " + str(time.time() - self.t1) + "с."
                                            self.ui.plainTextEdit.appendPlainText(self.str)
        #удаление индикатора после его работыtyu
        self.progress.deleteLater()


    def wordFive(self):
        pass

    def arrOutput(self, arr):
        arr.sort()
        self.str = ''
        for i in range(0, len(arr)):
            if i != len(arr) - 1:
                self.str += arr[i] + ', '
            else:
                self.str += arr[i] + '.'
        return self.str

    def clearText(self):
        self.ui.plainTextEdit.clear()

    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Enter:
            self.start1()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())