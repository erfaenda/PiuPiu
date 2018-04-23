import time

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow

from threading import Thread #Потоки
class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window,self).__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage('Ready')
    #Отображаем текст в статусбаре
    def setStatusBar(self,text):
        self.statusBar().showMessage(str(text))

class Main_Widget(QWidget):
    def __init__(self):
        super(Main_Widget,self).__init__()

class MyThread(Thread):
    def __init__(self,f):
        Thread.__init__(self)
        self.f = f
    def run(self):
        time.sleep(0.1)
        i = 0
        while True:
            text = str(i)
            i = i+1
            #Тут надо как-то вызвать смену текста статусбара
            self.f.message.emit(text)
            time.sleep(0.1)

class foo(QObject):
    message = pyqtSignal(str)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Main_Window()
    widget = Main_Widget()
    window.setCentralWidget(widget)
    window.show()
    f=foo()
    f.message.connect(window.setStatusBar)
    t = MyThread(f)
    t.start()
    sys.exit(app.exec_())