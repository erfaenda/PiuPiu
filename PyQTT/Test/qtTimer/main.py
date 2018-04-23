import sys, time
from datetime import timedelta, datetime
# Импортируем наш интерфейс из файла
from PyQTT.Test.qtTimer.gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer

class MyWin(QtWidgets.QMainWindow):

    # ports status
    sw_state1 = False
    sw_state2 = False
    sw_state3 = False
    sw_state4 = False

    # devices value
    temp_1 = 0
    temp_2 = 0
    middle_temp = 0
    gigro = 0

    # Logic value
    light = []
    ballu = []
    vlaga = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.uptime()

        # Здесь прописываем событие нажатия на кнопку
        self.ui.pushButton.clicked.connect(self.sw1_on)
        self.ui.pushButton_2.clicked.connect(self.sw1_off)
        self.ui.pushButton_3.clicked.connect(self.sw2_on)
        self.ui.pushButton_4.clicked.connect(self.sw2_off)
        self.ui.pushButton_5.clicked.connect(self.sw3_on)
        self.ui.pushButton_6.clicked.connect(self.sw3_off)
        self.ui.pushButton_7.clicked.connect(self.sw4_on)
        self.ui.pushButton_8.clicked.connect(self.sw4_off)

    def switch_light(self):
        a = self.ui.timeEdit.time()
        print(a.hour())Л


    def dateTime(self):
        #now = datetime.now()
        now = datetime.strftime(datetime.now(), "%H:%M:%S")
        self.ui.label_6.setText(str(now))

    def uptime(self):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds=uptime_seconds))

        self.ui.label.setText(uptime_string)

    def check_state(self):
        if self.sw_state1 == False:
            self.ui.label_2.setText('Порт № 1 - OFF')
        else:self.ui.label_2.setText('Порт № 1 - ON')
        if self.sw_state2 == False:
            self.ui.label_3.setText('Порт № 2 - OFF')
        else:self.ui.label_3.setText('Порт № 2 - ON')
        if self.sw_state3 == False:
            self.ui.label_4.setText('Порт № 3 - OFF')
        else:self.ui.label_4.setText('Порт № 3 - ON')
        if self.sw_state4 == False:
            self.ui.label_5.setText('Порт № 4 - OFF')
        else:self.ui.label_5.setText('Порт № 4 - ON')

    #def sw1_on(self, button, state):

    # buttons ON/OFF
    def sw1_on(self):
        time.sleep(0.2)
        # >>>some real work code<<<
        self.sw_state1 = True

    def sw1_off(self):
        time.sleep(0.2)
        # >>>some real work code<<<
        self.sw_state1 = False

    def sw2_on(self):
        time.sleep(0.2)
        # >>>some real work code<<<
        self.sw_state2 = True

    def sw2_off(self):
        time.sleep(0.2)
        # >>>some real work code<<<
        self.sw_state2 = False

    def sw3_on(self):
        time.sleep(0.2)
        # >>>some real work code<<<
        self.sw_state3 = True

    def sw3_off(self):
        time.sleep(0.2)
        # >>>some real work code<<<
        self.sw_state3 = False

    def sw4_on(self):
        time.sleep(0.2)
        # >>>some real work code<<<
        self.sw_state4 = True

    def sw4_off(self):
        time.sleep(0.2)
        # >>>some real work code<<<
        self.sw_state4 = False

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    timer = QTimer()
    timer.timeout.connect(myapp.check_state)
    timer.start(100)
    timeing = QTimer()
    timeing.timeout.connect(myapp.uptime)
    timeing.timeout.connect(myapp.dateTime)
    timeing.timeout.connect(myapp.switch_light)
    timeing.start(1000)
    myapp.show()
    sys.exit(app.exec_())