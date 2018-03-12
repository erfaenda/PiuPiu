import sys
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.show()

    def closeEvent(self, event):
        def closed():
            self.reply.close()
            event.ignore()

        self.reply = QDialog()
        vbox = QVBoxLayout()
        label_dialog = QLabel()
        label_dialog.setText('Вы действительно хотите выйти?')
        button_yes = QPushButton(self.reply)
        button_yes.setText("Да")
        button_yes.clicked.connect(lambda: self.reply.close())
        button_no = QPushButton(self.reply)
        button_no.setText('Нет')
        button_no.clicked.connect(closed)
        layout = QHBoxLayout()
        layout.addWidget(button_yes)
        layout.addWidget(button_no)
        vbox.addWidget(label_dialog)
        vbox.addSpacing(20)
        vbox.addLayout(layout)
        self.reply.setLayout(vbox)
        self.reply.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())