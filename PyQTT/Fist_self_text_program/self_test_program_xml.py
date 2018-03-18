import sys
import random
import xml.dom.minidom
# Импортируем наш интерфейс из файла
from PyQTT.Fist_self_text_program.self_test_programGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):

    text = []
    questions = []
    variants = []
    correct = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dom = xml.dom.minidom.parse('base.xml')
        self.collection = self.dom.documentElement
        self.linesArr = self.collection.getElementsByTagName("text")
        # Инициализирую  размер шрифта в текстовых полях
        self.ui.textEdit.setFontPointSize(12)
        self.ui.textEdit_2.setFontPointSize(14)
        self.ui.textEdit_3.setFontPointSize(16)

        for line in self.linesArr:
            self.text.append(line.childNodes[0].data)
            self.questions.append(line.getAttribute('question'))
            self.variants.append(line.getAttribute('answers').split('**?**'))
            self.correct.append(line.getAttribute('correct'))

        # Перетасовка вариантов
        random.shuffle(self.variants[0])
        random.shuffle(self.variants[1])
        random.shuffle(self.variants[2])

        # Возможно это позиционирование текста который надо изучить
        self.ui.textEdit.setHtml(self.text[0])
        self.ui.textEdit_2.setHtml(self.text[1])
        self.ui.textEdit_3.setHtml(self.text[2])
        # Позиционирование вопроса
        self.ui.label.setText(self.questions[0])
        self.ui.label_2.setText(self.questions[1])
        self.ui.label_3.setText(self.questions[2])

        # Перетасовка кнопок
        self.ui.radioButton.setText(self.variants[0][0])
        self.ui.radioButton_2.setText(self.variants[0][1])
        self.ui.radioButton_3.setText(self.variants[0][2])

        self.ui.radioButton_4.setText(self.variants[1][0])
        self.ui.radioButton_5.setText(self.variants[1][1])
        self.ui.radioButton_6.setText(self.variants[1][2])

        self.ui.radioButton_7.setText(self.variants[2][0])
        self.ui.radioButton_8.setText(self.variants[2][1])
        self.ui.radioButton_9.setText(self.variants[2][2])

        self.ui.Tab3.setTabEnabled(1, False)
        self.ui.Tab3.setTabEnabled(2, False)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.buttonGroup.buttonClicked.connect(self.correctAns1)
        self.ui.buttonGroup_2.buttonClicked.connect(self.correctAns2)
        self.ui.buttonGroup_3.buttonClicked.connect(self.correctAns3)
        #self.ui.pushButton.clicked.connect(self.MyFunction)
        #self.widget.keyPressEvent2.connect(self.MyFunction)


    # при нажатии на кнопку

    # Основные функции
    def correctAns1(self):
        for rb in self.ui.buttonGroup.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[0]:
                    self.ui.statusbar.showMessage("Ответ верный, вторая вкладка таблицы разблокирована!", 5000)
                    self.ui.tab_1.setEnabled(False)
                    self.ui.Tab3.setTabEnabled(1, True)

    def correctAns2(self):
        for rb in self.ui.buttonGroup_2.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[1]:
                    self.ui.statusbar.showMessage("Ответ верный, третья вкладка таблицы разблокирована!", 5000)
                    self.ui.tab_2.setEnabled(False)
                    self.ui.Tab3.setTabEnabled(2, True)

    def correctAns3(self):
        for rb in self.ui.buttonGroup_3.buttons():
            if rb.isChecked():
                if rb.text() == self.correct[2]:
                    self.ui.statusbar.showMessage("Ответ верный, вторая вкладка таблицы разблокирована!", 5000)
                    self.ui.tab_3.setEnabled(False)





if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())