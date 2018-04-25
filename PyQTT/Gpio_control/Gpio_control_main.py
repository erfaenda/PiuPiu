import sys, time
from datetime import timedelta, datetime
# Импортируем наш интерфейс из файла
from PyQTT.Gpio_control.gpio_gui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QStyleFactory

class MyWin(QtWidgets.QMainWindow):

    # ports status
    sw_state1 = False
    sw_state2 = False
    sw_state3 = False
    sw_state4 = False
    sw_state5 = False
    sw_state6 = False
    sw_state7 = False
    sw_state8 = False
    list_state =[sw_state1, sw_state2]

    # devices value
    temp_1 = 0
    temp_2 = 0
    middle_temp = 0
    gigro = 0

    # Logic state value
    deviceLogic_state = False
    timeLogic_state = False

    # Time logick value
    globalTime = 0
    dnat_min = 0
    dnat_max = 0

    light = []
    ballu = []
    vlaga = []

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.uptime()
        # signals and slots
        self.ui.pushButton.clicked.connect(self.sw1_on)
        self.ui.pushButton_2.clicked.connect(self.sw1_off)
        self.ui.pushButton_3.clicked.connect(self.sw2_on)
        self.ui.pushButton_4.clicked.connect(self.sw2_off)
        self.ui.pushButton_5.clicked.connect(self.sw3_on)
        self.ui.pushButton_6.clicked.connect(self.sw3_off)
        self.ui.pushButton_7.clicked.connect(self.sw4_on)
        self.ui.pushButton_8.clicked.connect(self.sw4_off)
        self.ui.pushButton_logic_on.clicked.connect(self.device_logicON)
        self.ui.pushButton_logic_off.clicked.connect(self.device_logicOFF)
        self.ui.pushButton_logicTimer_on.clicked.connect(self.time_logicON)
        self.ui.pushButton_logicTimer_off.clicked.connect(self.time_logicOFF)
    # test function
    def test(self):
        t1 = self.ui.timeEdit.time()
        now = datetime.now()
        today = now.replace(hour=t1.hour(), minute=t1.minute(), second=0, microsecond=0)

        print(now > today)

    # universal main fuction read time and control gpio ports
    def timer_logic(self):
        if self.timeLogic_state == True:
            time_min = self.ui.timeEdit.time()
            time_max = self.ui.timeEdit_2.time()
            now = datetime.now()
            self.dnat_min = now.replace(hour=time_min.hour(), minute=time_min.minute(), second=0, microsecond=0)
            self.dnat_max = now.replace(hour=time_max.hour(), minute=time_max.minute(), second=0, microsecond=0)
            # off range
            if now >= self.dnat_min and now <= self.dnat_max:
                self.sw1_off()
            else:
                self.sw1_on()

     # universal main fuction read time and control gpio ports
    def uni_timer_logic(self, time_min, time_max, sw_state):
        if self.timeLogic_state == True:
            if self.chekbox_list[chk]
            now = datetime.now()
            self.dnat_min = now.replace(hour=time_min.hour(), minute=time_min.minute(), second=0,
                                                    microsecond=0)
            self.dnat_max = now.replace(hour=time_max.hour(), minute=time_max.minute(), second=0,
                                                    microsecond=0)
            # off range
            if now >= self.dnat_min and now <= self.dnat_max:
                self.list_state[sw_state] = False
            else:
                self.list_state[sw_state] = True

    def starter_all_timer_logic(self):
        self.uni_timer_logic(self.ui.timeEdit.time(), self.ui.timeEdit_2.time(), 0)
        self.uni_timer_logic(self.ui.timeEdit_3.time(), self.ui.timeEdit_4.time(), 1)



    # main function read devices value and control gpio ports
    def deviceLogic(self):
        if self.deviceLogic_state == True:
            if self.middle_temp < self.ui.spinBoxOn_logic_1.value():
                self.sw1_on()
            if self.middle_temp > self.ui.spinBoxOff_logic_1.value():
                self.sw1_off()


    def switch_light(self):
        a = self.ui.timeEdit.time()
        print(a.hour() + a.minute())

    def readDevices(self):
        self.temp_1 = int(self.ui.temp1.text())
        self.temp_2 = int(self.ui.temp2.text())
        self.middle_temp = (self.temp_1 + self.temp_2) / 2
        self.ui.midtemp.setValue(self.middle_temp)


    def dateTime(self):
        # display time
        now = datetime.strftime(datetime.now(), "%H:%M:%S")
        self.ui.label_6.setText('Системное время: ' + str(now))
        time = datetime.now()
        #print('time ' + str(self.globalTime))
        print(self.list_state[0])

    def uptime(self):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds=uptime_seconds))

        self.ui.label.setText(uptime_string)

        # тут надо переписать как то модно
    '''def check_state_2(self):
        for state in self.list_state:
            if state == False:'''

    def check_state(self):
        # check state buttons on/off
        if self.list_state[0] == False:
            self.ui.label_status_port1.setText('OFF')
        else:
            self.ui.label_status_port1.setText('ON')
        if self.list_state[1] == False:
            self.ui.label_status_port2.setText('OFF')
        else:
            self.ui.label_status_port2.setText('ON')
        if self.sw_state3 == False:
            self.ui.label_status_port3.setText('OFF')
        else:
            self.ui.label_status_port3.setText('ON')
        if self.sw_state4 == False:
            self.ui.label_status_port4.setText('OFF')
        else:
            self.ui.label_status_port4.setText('ON')
        # check state logic on/off
        if self.deviceLogic_state == False:
            self.ui.label__status_logic.setText('Logic disable')
        else:
            self.ui.label__status_logic.setText('Logic enable')

        if self.timeLogic_state == False:
            self.ui.label_time_status.setText('Logic disable')
        else:
            self.ui.label_time_status.setText('Logic enable')

    def device_logicON(self):
        self.deviceLogic_state = True
        print(self.deviceLogic_state)

    def device_logicOFF(self):
        self.deviceLogic_state = False
        print(self.deviceLogic_state)

    def time_logicON(self):
        self.timeLogic_state = True

    def time_logicOFF(self):
        self.timeLogic_state = False

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
    app.setStyle(QStyleFactory.create('Oxygen'))
    myapp = MyWin()
    timer = QTimer()
    timer.timeout.connect(myapp.check_state)
    timer.start(100)
    timeing = QTimer()
    #timeing.timeout.connect(myapp.uptime)
    timeing.timeout.connect(myapp.dateTime)
    timeing.timeout.connect(myapp.switch_light)
    timeing.timeout.connect(myapp.readDevices)
    timeing.timeout.connect(myapp.deviceLogic)
    #timeing.timeout.connect(myapp.timer_logic)
    timeing.timeout.connect(myapp.starter_all_timer_logic)
    timeing.start(1000)
    myapp.show()
    sys.exit(app.exec_())
