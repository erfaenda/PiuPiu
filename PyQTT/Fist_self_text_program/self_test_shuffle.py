import sys
import random
# Импортируем наш интерфейс из файла
from PyQTT.Fist_self_text_program.self_test_programGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):

    correct = "2 + 2 = 4"
    correct2 = "Плоская Земля! Ну вы че епта! Ну плоская же она!"
    correct3 = "Вернее не только лишь все, мало кто может это делать"

    variants1 = [correct, 'На траве дрова', 'Путин 2018']
    variants2 = ['Шар', 'Квадрат', correct2]
    variants3 = [correct3, 'Кличко ты ли это','Украина це Европа']

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # блокирую вкладки таблицы
        self.ui.Tab3.setTabEnabled(1, False)
        self.ui.Tab3.setTabEnabled(2, False)

        # Перетасовка вариантов
        random.shuffle(self.variants1)
        random.shuffle(self.variants2)
        random.shuffle(self.variants3)

        # Перетасовка кнопок
        self.ui.radioButton.setText(self.variants1[0])
        self.ui.radioButton_2.setText(self.variants1[1])
        self.ui.radioButton_3.setText(self.variants1[2])

        self.ui.radioButton_4.setText(self.variants2[0])
        self.ui.radioButton_5.setText(self.variants2[1])
        self.ui.radioButton_6.setText(self.variants2[2])

        self.ui.radioButton_7.setText(self.variants3[0])
        self.ui.radioButton_8.setText(self.variants3[1])
        self.ui.radioButton_9.setText(self.variants3[2])

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
                if rb.text() == self.correct:
                    self.ui.statusbar.showMessage("Ответ верный, вторая вкладка таблицы разблокирована!", 5000)
                    self.ui.tab_1.setEnabled(False)
                    self.ui.Tab3.setTabEnabled(1, True)

    def correctAns2(self):
        for rb in self.ui.buttonGroup_2.buttons():
            if rb.isChecked():
                if rb.text() == self.correct:
                    self.ui.statusbar.showMessage("Ответ верный, вторая вкладка таблицы разблокирована!", 5000)
                    self.ui.tab_2.setEnabled(False)
                    self.ui.Tab3.setTabEnabled(2, True)

    def correctAns3(self):
        for rb in self.ui.buttonGroup_3.buttons():
            if rb.isChecked():
                if rb.text() == self.correct:
                    self.ui.statusbar.showMessage("Ответ верный, вторая вкладка таблицы разблокирована!", 5000)
                    self.ui.Tab3.setTabEnabled(2, False)





if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())