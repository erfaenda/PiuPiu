import sys
from PyQt5.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Example')
        self.setGeometry(300, 300, 300, 220)
        self.setWindowOpacity(0.6)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Example()
    w.show()

    sys.exit(app.exec_())