# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiChild_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Child_1(object):
    def setupUi(self, Child_1):
        Child_1.setObjectName("Child_1")
        Child_1.setWindowModality(QtCore.Qt.ApplicationModal)
        Child_1.resize(276, 173)
        Child_1.setWindowFlags(QtCore.Qt.Dialog)
        self.centralwidget = QtWidgets.QWidget(Child_1)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
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
        self.label.setText(_translate("Child_1", "Введите старый пароль"))
        self.pushButton_2.setText(_translate("Child_1", "Подтвердить"))
        self.pushButton.setText(_translate("Child_1", "Отменить"))

