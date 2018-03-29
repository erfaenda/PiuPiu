import sys
# Импортируем наш интерфейс из файла
from PyQTT.ComboBox.Combo import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        # Здесь прописываем событие нажатия на кнопку
        #self.ui.pushButton.clicked.connect(self.MyFunction)
        #self.widget.keyPressEvent2.connect(self.MyFunction)
        self.ui.comboBox.editTextChanged.connect(self.findText)

        # Инициализация списка содержимого в комбобоксе
        self.ui.comboBox.lineEdit()
        self.ui.comboBox.addItems(["Анастасия Литвиненко", "Александра", "Агафья Тулуповна", "Артензия", "Анюта", "Акинфеев", "Алоха",
                                  "Ариша", "Анаконда", "Агафонов Арогова", "Аграномов Аграномова"])


    def findText(self, s):
        index=self.ui.comboBox.findText(s)
        if index > -1:
            self.ui.comboBox.setCurrentIndex(index)

    # Пока пустая функция которая выполняется



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())