#!usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
import sys

app = QtGui.QApplication(sys.argv)

gb = QtGui.QGroupBox('РадиоКнопки')

rb1 = QtGui.QRadioButton('1')
rb2 = QtGui.QRadioButton('2')
rb3 = QtGui.QRadioButton('3')
bt = QtGui.QPushButton('Сброс')

vb = QtGui.QVBoxLayout()
vb.addWidget(rb1)
vb.addWidget(rb2)
vb.addWidget(rb3)
vb.addWidget(bt)

gb.setLayout(vb)

a = [rb1, rb2, rb3]


def sbros():
    for i in a:
        i.setCheckable(False)
        i.setCheckable(True)


bt.clicked.connect(sbros)