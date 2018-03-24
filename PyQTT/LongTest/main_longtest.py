import sys
import random
import os
import xml.dom.minidom
from PyQTT.LongTest.gui_long_test import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyWin(QtWidgets.QMainWindow):
    lbs = []
    rbs = [[''] * 10] * 15  # emply list 15x10
    bgrs = []
    labels = []
    variants = []
    correct = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # xml handling (read & mix)
        self.mixXml()
        # read to DOM
        self.readToDom()
        # assigning layout to the scrollarea
        self.verticalLayout = QtWidgets.QVBoxLayout(self.ui.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        # adding widgets to the scrollarea
        self.addWidgetsToInterface()
        self.ui.pushButton.clicked.connect(self.check)
    def mixXml(self):
        # read xml and mix the lines
        self.linesMixed = []
        self.r = open('questions.xml', 'r', encoding='utf-8')
        self.fileRead = self.r.readlines()
        for line in range(2, len(self.fileRead) - 1):
            self.linesMixed.append(self.fileRead[line])
            random.shuffle(self.linesMixed)
            self.r.close()
            # write temporary xml with new mixed lines
            self.w = open("temp.xml", 'w', encoding='utf-8')
            self.w.write('''<?xml version="1.0" encoding="utf-8"?>\n<content>\n''')
        for line in self.linesMixed:
            self.w.write('%s' % line)
            self.w.write('</content>')
            self.w.close()

    def readToDom(self):
        # read to DOM
        self.dom = xml.dom.minidom.parse('temp.xml')
        self.collection = self.dom.documentElement
        self.linesArr = self.collection.getElementsByTagName("q")
        for line in range(0, len(self.linesArr)):
            # label's text
            self.labels.append(self.linesArr[line].childNodes[0].data)
            # variants' text
            self.variants.append(self.linesArr[line].getAttribute('ans').split('**?**'))
            # correct answer
            self.correct.append(self.linesArr[line].getAttribute('cor'))
        # Mix variants
        for variant in self.variants:
            random.shuffle(variant)
            # Deleting temporary file
            os.remove('temp.xml')

    def addWidgetsToInterface(self):
    # adding widgets to the scrollarea
        for line in range(0, len(self.labels)):
            self.lbs.append(QtWidgets.QLabel(self.ui.scrollAreaWidgetContents))
            self.lbs[line].setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.lbs[line].setText('<b>%s</b>' % self.labels[line])
            self.verticalLayout.addWidget(self.lbs[line])
            self.bgrs.append(QtWidgets.QButtonGroup(self.ui.centralwidget))
        for v in range(0, len(self.variants[line])):
            self.rbs[line][v] = QtWidgets.QRadioButton(self.ui.scrollAreaWidgetContents)
            self.bgrs[line].addButton(self.rbs[line][v])
            self.rbs[line][v].setText(self.variants[line][v])
            self.verticalLayout.addWidget(self.rbs[line][v])
    def check(self):

        counter = 0
        for group in range(0, len(self.bgrs)):
            for rb in self.bgrs[group].buttons():
                if rb.isChecked():
                    if rb.text() == self.correct[group]:
                        counter += 1

                        # And this is the result! Rounded to 2 decimal points
                        message = "Your result is " + "%.2f" % float(counter / len(self.bgrs) * 100) + "%"
                        self.ui.statusbar.setStyleSheet('color: navy; font-weight: bold;')
                        self.ui.statusbar.showMessage(message)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())