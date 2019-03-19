from PyQt5.QtWidgets import QTableWidgetItem
from PyQTT.Tables.TableSetWidget.GUI import *
from PyQt5 import QtCore, QtWidgets
import sys

data = ['Python', 'PHP', 'Java']


class mywindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.exp)
        #self.ui.pushButton_2.clicked.connect(self.search)
        self.ui.pushButton_2.clicked.connect(self.getIndex)


        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(2)

        row = 0
        for item in data:
            cellinfo = QTableWidgetItem(item)

            line = QtWidgets.QLineEdit()
            line.setObjectName("line_row{}".format(row))
            line.setEchoMode(QtWidgets.QLineEdit.Password)
            line.setFocusPolicy(QtCore.Qt.NoFocus)
            line.setText(item)
            print(line.objectName())

            self.ui.tableWidget.setItem(row, 0, cellinfo)
            self.ui.tableWidget.setCellWidget(row, 1, line)

            #self.ui.tableWidget.setItem()
            row += 1
            line.selectionChanged.connect(lambda : print('A'))

    def search(self):
        for line in range(0, 3):
            str_1 = 'line_row{}'.format(line)
            abstract_line = self.findChild(QtCore.QObject, str_1)
            print(abstract_line.text())
            abstract_line.setText(str_1)

    def getIndex(self):
        for item in self.ui.tableWidget.selectedItems():
            print(item.text())



    def exp(self):
        row = 0
        for item in data:
            cellinfo = QTableWidgetItem(item)

            line = QtWidgets.QLineEdit()
            line.setObjectName("line_row{}".format(row))
            line.setEchoMode(QtWidgets.QLineEdit.Normal)
            #line.setFocusPolicy(QtCore.Qt.NoFocus)
            line.setText(item)

            self.ui.tableWidget.setItem(row, 0, cellinfo)
            self.ui.tableWidget.setCellWidget(row, 1, line)
            # self.ui.tableWidget.setItem()
            row += 1

app = QtWidgets.QApplication([])
win = mywindow()
win.show()

sys.exit(app.exec())