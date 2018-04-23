import sys, time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QSizePolicy, QApplication


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        self.my_counter = 1

        QWidget.__init__(self, *args, **kwargs)

        self.label = QLabel("QLabel", self)
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("QLabel {background-color: pink; font-size: 50pt;}")

        self.button = QPushButton("Test", self)

        self.button.clicked.connect(self.local_button_handler)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0)
        self.layout.addWidget(self.button, 0, 1)

        self.setLayout(self.layout)
        self.show()

    def local_button_handler(self):
        self.label.setText("Qlabel" + " %d tick" % self.my_counter)
        self.my_counter += 1

    def func2(self):
        self.label.setText('ПОток 2')

app = QApplication(sys.argv)
win = Window()

timer = QTimer()
timer2 = QTimer()
timer.timeout.connect(win.local_button_handler)
timer2.timeout.connect(win.func2)
timer.start(100)
timer2.start(100)
sys.exit(app.exec_())