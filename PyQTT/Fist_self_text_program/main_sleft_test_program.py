import sys
# Импортируем наш интерфейс из файла
from PyQTT.Fist_self_text_program.self_test_programGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # блокирую вкладки таблицы
        self.ui.Tab3.setTabEnabled(1, False)
        self.ui.Tab3.setTabEnabled(2, False)

        # Здесь прописываем событие нажатия на кнопку
        self.ui.radioButton.clicked.connect(self.correctAns1)
        self.ui.radioButton_6.clicked.connect(self.correctAns2)
        self.ui.radioButton_7.clicked.connect(self.correctAns3)
        #self.ui.pushButton.clicked.connect(self.MyFunction)
        #self.widget.keyPressEvent2.connect(self.MyFunction)


    # при нажатии на кнопку

    # Основные функции
    def correctAns1(self):
        self.ui.statusbar.showMessage("Ответ верный, вторая вкладка таблицы разблокирована!", 5000)
        self.ui.tab_1.setEnabled(False)
        self.ui.Tab3.setTabEnabled(1, True)

    def correctAns2(self):
        self.ui.statusbar.showMessage("Ответ верный, вторая вкладка таблицы разблокирована!", 5000)
        self.ui.tab_2.setEnabled(False)
        self.ui.Tab3.setTabEnabled(2, True)

    def correctAns3(self):
        self.ui.statusbar.showMessage("Ответ верный, вторая вкладка таблицы разблокирована!", 5000)
        self.ui.tab_3.setEnabled(False)
        #self.ui.Tab3.setTabEnabled(1, True)





if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())