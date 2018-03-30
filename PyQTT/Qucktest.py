import sys
from PyQt5 import QtWidgets

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QWidget.__init__(self)
        self.combo = QtWidgets.QComboBox(self)
        self.combo.setEditable(True)
        self.combo.editTextChanged.connect(self.findText)
        #self.combo.currentTextChanged.connect(self.findText)
        self.combo.addItems([u"Петров", u"Сидоров", u"Иванов", u"Ивановa", "a.silantev", "a.alena", "a.olega", "a.pizda", "a.agafya", "a.prostitute",
                             "a.aleninka", "a.alenko"])
        self.show()

    def findText(self, s):
        index=self.combo.findText(s)
        if index > -1:
            self.combo.setCurrentIndex(index)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


