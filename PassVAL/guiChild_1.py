# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiChild_1.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Child_1(object):
    def setupUi(self, Child_1):
        Child_1.setObjectName("Child_1")
        Child_1.setWindowModality(QtCore.Qt.WindowModal)
        Child_1.resize(276, 173)
        self.centralwidget = QtWidgets.QWidget(Child_1)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        Child_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(Child_1)
        QtCore.QMetaObject.connectSlotsByName(Child_1)

    def retranslateUi(self, Child_1):
        _translate = QtCore.QCoreApplication.translate
        Child_1.setWindowTitle(_translate("Child_1", "Смена мастер пароля"))
        self.pushButton_2.setText(_translate("Child_1", "PushButton"))
        self.pushButton.setText(_translate("Child_1", "PushButton"))

