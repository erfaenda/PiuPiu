import sys
# Импортируем наш интерфейс из файла
from PyQTT.ComboBox.Combo import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
ва
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.editTextChanged.connect(self.findText)
        self.ui.comboBox.editTextChanged.connect(self.pupUp)


        # Инициализация списка содержимого в комбобоксе
        self.ui.comboBox.addItem('')
        self.ui.comboBox.addItems(["Анастасия Литвиненко", "Александра", "Агафья Тулуповна", "Артензия", "Анюта", "Акинфеев", "Алоха",
                                  "Ариша", "Анаконда", "Агафонов Арогова", "Аграномов Аграномова"])
        self.ui.comboBox.view()

    def pupUp(self):
        if self.ui.comboBox.editTextChanged():
            self.ui.comboBox.showPopup()
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