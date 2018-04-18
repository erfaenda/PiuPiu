from PyQt5 import Qt


class Widget(Qt.QWidget):

    def __init__(self):
        super().__init__()
        layout = Qt.QHBoxLayout(self)
        table = Qt.QTableWidget()
        table.setRowCount(2)
        table.setColumnCount(2)
        btn = Qt.QPushButton("Добавить")
        btn2 = Qt.QPushButton("Редактировать")
        table.setCellWidget(1, 0, btn)
        table.setCellWidget(0, 1, btn2)
        table.resizeColumnsToContents() # выравнивание по наличию контента
        #table.setEnabled(False)
        table.setEditTriggers(table.NoEditTriggers)
        #self.tableName.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        layout.addWidget(table)
        btn2.clicked.connect(lambda: table.setEditTriggers())
        #btn2.clicked.connect(lambda : self.setEnabled(False))


if __name__ == '__main__':
    app = Qt.QApplication([])
    w = Widget()
    w.show()
    app.exec()