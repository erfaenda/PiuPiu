from PyQt5.QtWidgets import QApplication, QMainWindow, QProgressBar
from PyQt5.QtCore import pyqtSignal, QTimer
from threading import Thread
from time import sleep

def work(data):
    '''работа - каждые 0.5 сек уменьшать data'''
    while data:
        sleep(.5)
        data.pop()
        # обновить прогресс можно тут, тк dataLen это pyqtSignal, и можно обновлять gui из любого потока
        # минус в том что будет вызвано len(data)=100 обновлений прогресбара
        Wnd.dataLen.emit(len(data))

class Window(QMainWindow):
    '''прогресс длины списка data_'''
    dataLen = pyqtSignal(int)

    def __init__(self, data):
        QMainWindow.__init__(self)
        self.bar = QProgressBar(self)
        self.setCentralWidget(self.bar)

        self.data = data
        self.bar.setValue(len(data))
        # установить значение dataLen в bar
        self.dataLen.connect(self.bar.setValue)

        # если не использовать dataLen, то можно обновлять прогресбар, каждые x секунд по таймеру
    #     self.timer = QTimer()
    #     self.timer.timeout.connect(self.update_bar)  # по истечению таймаута запустить self.update_bar
    #     self.update_bar()
    #
    # def update_bar(self):
    #     '''обновлять прогресбар каждые 3 сек'''
    #     data_len = len(self.data)
    #     self.bar.setValue(data_len)
    #     if data_len:
    #         self.timer.start(3000)  # установить таймер

if __name__ == '__main__':
    qa = QApplication([])

    data_ = list(range(100))
    Wnd = Window(data_)
    Thread(target=work, args=[data_]).start()  # работать в потоке

    Wnd.show()
    qa.exec_()