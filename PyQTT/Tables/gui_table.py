# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_table.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(932, 592)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 911, 271))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 7, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 290, 911, 71))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 360, 131, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 360, 111, 34))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        self.tableWidget.cellChanged['int','int'].connect(self.tableWidget.resizeColumnsToContents)
        self.tableWidget_2.cellChanged['int','int'].connect(self.tableWidget_2.resizeColumnsToContents)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Акт"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Имя хоста"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Инвентарны номер"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "От кого"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Кому"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Примечание"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "ip адрес"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Дата"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "eis"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "2233"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("Form", "ЭИС"))
        item = self.tableWidget.item(0, 4)
        item.setText(_translate("Form", "СМЭВ"))
        item = self.tableWidget.item(0, 5)
        item.setText(_translate("Form", "Просто тест"))
        item = self.tableWidget.item(0, 6)
        item.setText(_translate("Form", "10.9.9.9"))
        item = self.tableWidget.item(0, 7)
        item.setText(_translate("Form", "10.01.2018"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Имя хоста"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Инвентарный номер"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "От кого"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Кому"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Примечание"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "ip адрес"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Дата"))
        self.pushButton.setText(_translate("Form", "Редактировать"))
        self.pushButton_2.setText(_translate("Form", "Добавить"))

