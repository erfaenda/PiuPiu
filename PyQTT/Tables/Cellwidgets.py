from PyQt5 import Qt


class Widget(Qt.QWidget):
    table = Qt.QTableWidget()
    def __init__(self):
        super().__init__()
        layout = Qt.QHBoxLayout(self)
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        btn = Qt.QPushButton("Добавить")
        btn2 = Qt.QPushButton("Редактировать")
        self.table.setCellWidget(1, 0, btn)
        self.table.setCellWidget(0, 1, btn2)
        self.table.resizeColumnsToContents() # выравнивание по наличию контента
        #table.setEnabled(False)
        self.table.setEditTriggers(self.table.NoEditTriggers)
        layout.addWidget(self.table)
        #btn2.clicked.connect(self.Editable)

    def Editable(self):
        self.table.setEditTriggers(self.table.DoubleClicked)





if __name__ == '__main__':
    app = Qt.QApplication([])
    w = Widget()
    w.show()
    app.exec()