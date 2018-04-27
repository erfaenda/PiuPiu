# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(322, 138)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 10, 101, 34))
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 191, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 60, 301, 18))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Do something"))
        self.comboBox.setItemText(0, _translate("Form", "Первая функция"))
        self.comboBox.setItemText(1, _translate("Form", "Вторая функция"))
        self.label.setText(_translate("Form", "Какая функция будет выполнятся?"))

