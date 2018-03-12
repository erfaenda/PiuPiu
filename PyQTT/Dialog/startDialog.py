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
    # Стандарный  вызов диалога
    '''def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self, "Подтверждение", "Хотите выйти?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                            QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()'''
    # Кастомное окно диалога, можно переназначать текст кнопок и названия
    def closeEvent(self, event):
        def closed():
            self.reply.close()
            event.ignore()

        self.reply = QDialog()
        vbox = QVBoxLayout()
        label_dialog = QLabel()
        label_dialog.setText('Вы действительно хотите выйти?')
        button_yes = QPushButton(self.reply)
        button_yes.setText("Да")
        button_yes.clicked.connect(lambda: self.reply.close())
        button_no = QPushButton(self.reply)
        button_no.setText('Нет')
        button_no.clicked.connect(closed)
        layout = QHBoxLayout()
        layout.addWidget(button_yes)
        layout.addWidget(button_no)
        vbox.addWidget(label_dialog)
        vbox.addSpacing(20)
        vbox.addLayout(layout)
        self.reply.setLayout(vbox)
        self.reply.exec()

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