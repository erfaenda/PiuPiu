import sys
# Импортируем наш интерфейс из файла
from PyQTT.Dialog.dialogGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionSave.triggered.connect(self.saveToFile)
        self.ui.actionOpen.triggered.connect(self.openFile)
    # Стандарный  вызов диалога
    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Подтверждение", "Хотите выйти?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No |
                                            QtWidgets.QMessageBox.Cancel)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()
        # простое сохранение в уготованный файл
    '''def saveToFile(self):
        self.writeFile = open("text.txt", 'w', encoding='utf-8')
        self.writeFile.write(self.ui.plainTextEdit.toPlainText())
        self.writeFile.close()'''
    # запись в файл по выбору с выбором имени
    def saveToFile(self):
        options = QtWidgets.QFileDialog.Options()
        self.fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить в ", "", "HTML Files (*.html)", options=options)
        if self.fileName:
            self.writeFile = open(self.fileName, 'w', encoding='utf-8')
            self.writeFile.write(self.ui.plainTextEdit.toHtml())
            self.writeFile.close()
            self.ui.statusbar.showMessage('Сохранено в... {}'.format(self.fileName))

    def openFile(self):
        options = QtWidgets.QFileDialog.Options()
        self.fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open File", '', 'HTML Files (*.html)', options=options)
        if self.fileName:
            self.openF = open(self.fileName, 'r', encoding='utf-8')
            self.ui.plainTextEdit.insertPlainText(self.openF.read())
            self.openF.close()
            self.ui.statusbar.showMessage('{} открыт'.format(self.fileName))

# при нажатии на кнопку
    def myfunction(self):
        self.ui.label.setText("Длинна вашего текста {} символов(а)".format(len(self.ui.lineEdit.text())))

    # отслеживаю нажатие  ентера и выполняю функцию
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Enter:
            self.myfunction()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())