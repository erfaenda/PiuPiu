# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iCaclsGUI_2.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1027, 814)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../Trash/tmp/icona.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setStyleSheet("background:rgb(165, 221, 255)")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setStyleSheet("background:rgb(165, 221, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.checkBox_33 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_33.setObjectName("checkBox_33")
        self.gridLayout.addWidget(self.checkBox_33, 2, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 2)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_18 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_18.setObjectName("checkBox_18")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.checkBox_18)
        self.gridLayout_2.addWidget(self.checkBox_18, 2, 2, 1, 1)
        self.checkBox_15 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_15.setObjectName("checkBox_15")
        self.buttonGroup_3.addButton(self.checkBox_15)
        self.gridLayout_2.addWidget(self.checkBox_15, 1, 2, 1, 1)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_8.setObjectName("checkBox_8")
        self.buttonGroup_3.addButton(self.checkBox_8)
        self.gridLayout_2.addWidget(self.checkBox_8, 7, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.buttonGroup_3.addButton(self.checkBox_2)
        self.gridLayout_2.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.checkBox_19 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_19.setObjectName("checkBox_19")
        self.buttonGroup_3.addButton(self.checkBox_19)
        self.gridLayout_2.addWidget(self.checkBox_19, 0, 2, 1, 1)
        self.checkBox_14 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_14.setObjectName("checkBox_14")
        self.buttonGroup_3.addButton(self.checkBox_14)
        self.gridLayout_2.addWidget(self.checkBox_14, 6, 2, 1, 1)
        self.checkBox_20 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_20.setObjectName("checkBox_20")
        self.buttonGroup_3.addButton(self.checkBox_20)
        self.gridLayout_2.addWidget(self.checkBox_20, 8, 2, 1, 1)
        self.checkBox_17 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_17.setObjectName("checkBox_17")
        self.buttonGroup_3.addButton(self.checkBox_17)
        self.gridLayout_2.addWidget(self.checkBox_17, 5, 2, 1, 1)
        self.checkBox_11 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_11.setObjectName("checkBox_11")
        self.buttonGroup_3.addButton(self.checkBox_11)
        self.gridLayout_2.addWidget(self.checkBox_11, 9, 2, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setObjectName("checkBox_7")
        self.buttonGroup_3.addButton(self.checkBox_7)
        self.gridLayout_2.addWidget(self.checkBox_7, 6, 0, 1, 1)
        self.checkBox_12 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_12.setObjectName("checkBox_12")
        self.buttonGroup_3.addButton(self.checkBox_12)
        self.gridLayout_2.addWidget(self.checkBox_12, 7, 2, 1, 1)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_10.setObjectName("checkBox_10")
        self.buttonGroup_3.addButton(self.checkBox_10)
        self.gridLayout_2.addWidget(self.checkBox_10, 9, 0, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.buttonGroup_3.addButton(self.checkBox_6)
        self.gridLayout_2.addWidget(self.checkBox_6, 5, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.buttonGroup_3.addButton(self.checkBox)
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.buttonGroup_3.addButton(self.checkBox_4)
        self.gridLayout_2.addWidget(self.checkBox_4, 3, 0, 1, 1)
        self.checkBox_9 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_9.setObjectName("checkBox_9")
        self.buttonGroup_3.addButton(self.checkBox_9)
        self.gridLayout_2.addWidget(self.checkBox_9, 8, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 4, 3, 1, 1)
        self.checkBox_13 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_13.setObjectName("checkBox_13")
        self.buttonGroup_3.addButton(self.checkBox_13)
        self.gridLayout_2.addWidget(self.checkBox_13, 3, 2, 1, 1)
        self.checkBox_16 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_16.setObjectName("checkBox_16")
        self.buttonGroup_3.addButton(self.checkBox_16)
        self.gridLayout_2.addWidget(self.checkBox_16, 4, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 1, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.buttonGroup_3.addButton(self.checkBox_5)
        self.gridLayout_2.addWidget(self.checkBox_5, 4, 0, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.buttonGroup_3.addButton(self.checkBox_3)
        self.gridLayout_2.addWidget(self.checkBox_3, 2, 0, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 2, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setStyleSheet("background:rgb(165, 221, 255)")
        self.pushButton_4.setObjectName("pushButton_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.pushButton_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole, spacerItem2)
        self.checkBox_26 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_26.setObjectName("checkBox_26")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.checkBox_26)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox_26)
        self.checkBox_27 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_27.setObjectName("checkBox_27")
        self.buttonGroup.addButton(self.checkBox_27)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_27)
        self.checkBox_28 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_28.setObjectName("checkBox_28")
        self.buttonGroup.addButton(self.checkBox_28)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_28)
        self.checkBox_29 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_29.setObjectName("checkBox_29")
        self.buttonGroup.addButton(self.checkBox_29)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_29)
        self.checkBox_31 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_31.setObjectName("checkBox_31")
        self.buttonGroup.addButton(self.checkBox_31)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.checkBox_31)
        self.checkBox_32 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_32.setObjectName("checkBox_32")
        self.buttonGroup.addButton(self.checkBox_32)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkBox_32)
        self.checkBox_30 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_30.setObjectName("checkBox_30")
        self.buttonGroup.addButton(self.checkBox_30)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkBox_30)
        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setStyleSheet("background:rgb(165, 221, 255)")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setStyleSheet("background:rgb(255, 210, 138)")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setStyleSheet("background:rgb(165, 221, 255)")
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setStyleSheet("background:rgb(255, 210, 138)")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.checkBox_22 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_22.setObjectName("checkBox_22")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.checkBox_22)
        self.gridLayout_4.addWidget(self.checkBox_22, 1, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 34))
        self.pushButton_3.setMaximumSize(QtCore.QSize(156, 34))
        self.pushButton_3.setBaseSize(QtCore.QSize(156, 34))
        self.pushButton_3.setStyleSheet("background:rgb(255, 210, 138)")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 1, 4, 1, 1)
        self.checkBox_21 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_21.setObjectName("checkBox_21")
        self.buttonGroup_2.addButton(self.checkBox_21)
        self.gridLayout_4.addWidget(self.checkBox_21, 0, 0, 1, 1)
        self.checkBox_25 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_25.setObjectName("checkBox_25")
        self.buttonGroup_2.addButton(self.checkBox_25)
        self.gridLayout_4.addWidget(self.checkBox_25, 0, 2, 1, 3)
        self.checkBox_24 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_24.setObjectName("checkBox_24")
        self.buttonGroup_2.addButton(self.checkBox_24)
        self.gridLayout_4.addWidget(self.checkBox_24, 1, 1, 1, 1)
        self.checkBox_23 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_23.setObjectName("checkBox_23")
        self.buttonGroup_2.addButton(self.checkBox_23)
        self.gridLayout_4.addWidget(self.checkBox_23, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 3, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_3, 3, 0, 1, 2)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background:rgb(37, 53, 44);color: rgb(212, 255, 212)\n"
"")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_3.addWidget(self.plainTextEdit, 5, 0, 1, 2)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setStyleSheet("background:rgb(210, 213, 217)")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1027, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iCacls Shell alpha"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Путь к папке или файлу"))
        self.label.setText(_translate("MainWindow", "SID:"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать директорию"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Введите имя пользователя или группы"))
        self.pushButton_2.setText(_translate("MainWindow", "Найти"))
        self.checkBox_33.setText(_translate("MainWindow", "Local"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Список отдельных прав:"))
        self.checkBox_18.setText(_translate("MainWindow", "WD - Запись данных, добавление файлов"))
        self.checkBox_15.setText(_translate("MainWindow", "RD - Чтение данных, перечисление содержимого папки"))
        self.checkBox_8.setText(_translate("MainWindow", "GR - Общее чтение"))
        self.checkBox_2.setText(_translate("MainWindow", "RC - Чтение"))
        self.checkBox_19.setText(_translate("MainWindow", "GA - Все общие"))
        self.checkBox_14.setText(_translate("MainWindow", "X - Выполнение файлов и обзор папок"))
        self.checkBox_20.setText(_translate("MainWindow", "RA - чтение атрибутов"))
        self.checkBox_17.setText(_translate("MainWindow", "WEA - Запись дополнительных атрибутов"))
        self.checkBox_11.setText(_translate("MainWindow", "WA - Запись атрибутов"))
        self.checkBox_7.setText(_translate("MainWindow", "MA - Максимально возможный"))
        self.checkBox_12.setText(_translate("MainWindow", "DC - Удаление вложенных объектов"))
        self.checkBox_10.setText(_translate("MainWindow", "GE - Общее выполнение"))
        self.checkBox_6.setText(_translate("MainWindow", "AS - Доступ к безопасности системы"))
        self.checkBox.setText(_translate("MainWindow", "DE - Доступ отсутствует"))
        self.checkBox_4.setText(_translate("MainWindow", "WO - Смена владельца"))
        self.checkBox_9.setText(_translate("MainWindow", "GW - Общая запись"))
        self.checkBox_13.setText(_translate("MainWindow", "AD - Добавление файлов и вложенных каталогов"))
        self.checkBox_16.setText(_translate("MainWindow", "REA - Чтение дополнительных атрибутов"))
        self.checkBox_5.setText(_translate("MainWindow", "S - Синхронизация"))
        self.checkBox_3.setText(_translate("MainWindow", "WDAC - запись DAC"))
        self.groupBox.setTitle(_translate("MainWindow", "Последовательность простых прав:"))
        self.pushButton_4.setText(_translate("MainWindow", "Очистить"))
        self.checkBox_26.setText(_translate("MainWindow", "&N - Доступ отсутствует"))
        self.checkBox_27.setText(_translate("MainWindow", "F - Полный доступ"))
        self.checkBox_28.setText(_translate("MainWindow", "M - доступ на изменение"))
        self.checkBox_29.setText(_translate("MainWindow", "R&X - Доступ на чтение и выполнение"))
        self.checkBox_31.setText(_translate("MainWindow", "R - Доступ только на чтение"))
        self.checkBox_32.setText(_translate("MainWindow", "W - Доступ только на запись"))
        self.checkBox_30.setText(_translate("MainWindow", "&D - доступ на удаление"))
        self.pushButton_8.setText(_translate("MainWindow", "Проверить права"))
        self.pushButton_7.setText(_translate("MainWindow", "Отключить наследование"))
        self.pushButton_6.setText(_translate("MainWindow", "Стасть владельцем"))
        self.pushButton_5.setText(_translate("MainWindow", "Забрать все права"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Права наследования:"))
        self.checkBox_22.setText(_translate("MainWindow", "CI - Наследование контейнерами"))
        self.pushButton_3.setText(_translate("MainWindow", "Назначить"))
        self.checkBox_21.setText(_translate("MainWindow", "OI - Наследование объектами"))
        self.checkBox_25.setText(_translate("MainWindow", "I - Наследование разрешений от родительского контейнера"))
        self.checkBox_24.setText(_translate("MainWindow", "NP - Запрет на распространение наследования"))
        self.checkBox_23.setText(_translate("MainWindow", "IO - Только наследование"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.pushButton_9.setText(_translate("MainWindow", "Очистить вывод"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.action.setText(_translate("MainWindow", "Выход"))

