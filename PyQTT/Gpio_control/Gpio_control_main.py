#import RPi.GPIO as GPIO
import sys, time, os
from datetime import timedelta, datetime
from PyQTT.Gpio_control.gpio_gui import *
from PyQTT.Gpio_control.gpio_child import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QStyleFactory

class MyWin(QtWidgets.QMainWindow):

    '''# initial port GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.IN)
    GPIO.setup(17, GPIO.IN)
    GPIO.setup(27, GPIO.IN)
    GPIO.setup(22, GPIO.IN)'''

    # ports status
    sw_state1 = False
    sw_state2 = False
    sw_state3 = False
    sw_state4 = False
    sw_state5 = False
    sw_state6 = False
    sw_state7 = False
    sw_state8 = False
    list_state = [sw_state1, sw_state2, sw_state3, sw_state4, sw_state5, sw_state6, sw_state7, sw_state8]
    list_checkboxes_time_logic = []

    # devices value
    list_devices = ['Средняя температура', 'Температура 1','Температура 2','Гигрометр 1','Гигрометр 2',
                    'Средняя влажность ']
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

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.uptime()
        self.append_list_checkboxes()
        self.ui.buttonGroup.setExclusive(False)
        # signals and slots
        #self.ui.pushButton.clicked.connect(self.sw1_on)
        self.ui.pushButton_logic_on.clicked.connect(self.device_logicON)
        self.ui.pushButton_logic_off.clicked.connect(self.device_logicOFF)
        self.ui.pushButton_logicTimer_on.clicked.connect(self.time_logicON)
        self.ui.pushButton_logicTimer_off.clicked.connect(self.time_logicOFF)
        self.ui.btn_time_logic_editNames.clicked.connect(self.show_child_window)
        self.ui.pushButton.clicked.connect(lambda: self.sw_on(0))
        self.ui.pushButton_2.clicked.connect(lambda: self.sw_off(0))
        self.ui.pushButton_3.clicked.connect(lambda: self.sw_on(1))
        self.ui.pushButton_4.clicked.connect(lambda: self.sw_off(1))
        self.ui.pushButton_5.clicked.connect(lambda: self.sw_on(2))
        self.ui.pushButton_6.clicked.connect(lambda: self.sw_off(2))
        self.ui.pushButton_7.clicked.connect(lambda: self.sw_on(3))
        self.ui.pushButton_8.clicked.connect(lambda: self.sw_off(3))
        self.ui.pushButton_9.clicked.connect(lambda: self.sw_on(4))
        self.ui.pushButton_10.clicked.connect(lambda: self.sw_off(4))
        self.ui.pushButton_11.clicked.connect(lambda: self.sw_on(5))
        self.ui.pushButton_12.clicked.connect(lambda: self.sw_off(5))
        self.ui.pushButton_13.clicked.connect(lambda: self.sw_on(6))
        self.ui.pushButton_14.clicked.connect(lambda: self.sw_off(6))
        self.ui.pushButton_15.clicked.connect(lambda: self.sw_on(7))
        self.ui.pushButton_16.clicked.connect(lambda: self.sw_off(7))

    def sw_on(self, sw_state):
        if self.list_state[sw_state] == False:
            self.list_state[sw_state] = True

    def sw_off(self, sw_state):
        if self.list_state[sw_state] == True:
            self.list_state[sw_state] = False

    # show_child_window
    def show_child_window(self):
        #child_window.ui.lineEdit.setText(self.ui.label_10.text())
        child_window.show()

    # Поиск по именам объектов.... магия
    def Save_change(self):
        for line in range(1, 9):
            str_1 = 'label_time_logic_{}'.format(line)
            str_2 = 'lineEdit_{}'.format(line)
            str_3 = 'label_device_logic_{}'.format(line)
            abstract_line = self.findChild(QtCore.QObject, str_1)
            abstract_lineEdit = child_window.findChild(QtCore.QObject, str_2)
            abstract_label_device_logic = self.findChild(QtCore.QObject, str_3)
            abstract_line.setText(abstract_lineEdit.text())
            abstract_label_device_logic.setText(abstract_lineEdit.text())


    # main fuction read time and control gpio ports, not used
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
    def uni_timer_logic(self, time_min, time_max, sw_state, checkbox_in_list, combobox):
        if self.timeLogic_state == True:
            if self.list_checkboxes_time_logic[checkbox_in_list].isChecked():
                now = datetime.now()
                self.dnat_min = now.replace(hour=time_min.hour(), minute=time_min.minute(), second=0,
                                                                microsecond=0)
                self.dnat_max = now.replace(hour=time_max.hour(), minute=time_max.minute(), second=0,
                                                                microsecond=0)
                # off range and on range
                if combobox.currentIndex() == 1:
                    if now >= self.dnat_min and now <= self.dnat_max:
                        self.list_state[sw_state] = False
                    else:
                        self.list_state[sw_state] = True
                else:
                    if now >= self.dnat_min and now <= self.dnat_max:
                        self.list_state[sw_state] = True
                    else:
                        self.list_state[sw_state] = False

    def append_list_checkboxes(self):
        for i in range(1,9):
            str_1 = 'checkBox_time_logic_{}'.format(i)
            abstract_chkbx = self.findChild(QtCore.QObject, str_1)
            self.list_checkboxes_time_logic.append(abstract_chkbx)


    # function starter ACHTUNG! shitcode
    def starter_all_timer_logic(self):
        self.uni_timer_logic(self.ui.timeEdit.time(), self.ui.timeEdit_2.time(), 0, 0, self.ui.comboBox)
        self.uni_timer_logic(self.ui.timeEdit_3.time(), self.ui.timeEdit_4.time(), 1, 1, self.ui.comboBox_2)
        self.uni_timer_logic(self.ui.timeEdit_7.time(), self.ui.timeEdit_8.time(), 2, 2, self.ui.comboBox_3)
        self.uni_timer_logic(self.ui.timeEdit_5.time(), self.ui.timeEdit_6.time(), 3, 3, self.ui.comboBox_4)
        self.uni_timer_logic(self.ui.timeEdit_18.time(), self.ui.timeEdit_17.time(), 4, 4, self.ui.comboBox_5)
        self.uni_timer_logic(self.ui.timeEdit_20.time(), self.ui.timeEdit_19.time(), 5, 5, self.ui.comboBox_6)
        self.uni_timer_logic(self.ui.timeEdit_24.time(), self.ui.timeEdit_23.time(), 6, 6, self.ui.comboBox_7)
        self.uni_timer_logic(self.ui.timeEdit_26.time(), self.ui.timeEdit_25.time(), 7, 7, self.ui.comboBox_8)

    # main function read devices value and control gpio ports
    def deviceLogic(self):
        if self.deviceLogic_state == True:
            if self.middle_temp < self.ui.spinBoxOn_logic_1.value():
                self.sw_on(0)
            if self.middle_temp > self.ui.spinBoxOff_logic_1.value():
                self.sw_off(0)

    def switch_light(self):
        a = self.ui.timeEdit.time()
        #print(a.hour() + a.minute())

    # read devices values and show they
    def readDevices(self):
        self.temp_1 = int(self.ui.temp1.text())
        self.temp_2 = int(self.ui.temp2.text())
        self.middle_temp = (self.temp_1 + self.temp_2) / 2
        self.ui.midtemp.setValue(self.middle_temp)

    # temp raspberry
    def measure_temp(self):
        temp = os.popen("vcgencmd measure_temp").readline()
        a = temp.replace("temp=", "")
        s = a[0:2]
        i = int(s)
        self.ui.midtemp.setValue(i)

    def dateTime(self):
        # display time
        now = datetime.strftime(datetime.now(), "%H:%M:%S")
        self.ui.label_6.setText('Системное время: ' + str(now))
        time = datetime.now()
        #print('time ' + str(self.globalTime))
        #print(self.list_state[0])

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
        # это гавно надо переписать
        if self.list_state[0] == False:
            time.sleep(0.5)
            self.ui.label_status_port1.setText('OFF')
            #GPIO.setup(4, GPIO.IN)
        else:
            time.sleep(0.5)
            self.ui.label_status_port1.setText('ON')
            #GPIO.setup(4, GPIO.OUT)

        if self.list_state[1] == False:
            self.ui.label_status_port2.setText('OFF')
        else:
            self.ui.label_status_port2.setText('ON')
        if self.list_state[2] == False:
            self.ui.label_status_port3.setText('OFF')
        else:
            self.ui.label_status_port3.setText('ON')
        if self.list_state[3] == False:
            self.ui.label_status_port4.setText('OFF')
        else:
            self.ui.label_status_port4.setText('ON')
        if self.list_state[4] == False:
            self.ui.label_status_port5.setText('OFF')
        else:
            self.ui.label_status_port5.setText('ON')
        if self.list_state[5] == False:
            self.ui.label_status_port6.setText('OFF')
        else:
            self.ui.label_status_port6.setText('ON')
        if self.list_state[6] == False:
            self.ui.label_status_port7.setText('OFF')
        else:
            self.ui.label_status_port7.setText('ON')
        if self.list_state[7] == False:
            self.ui.label_status_port8.setText('OFF')
        else:
            self.ui.label_status_port8.setText('ON')

        # check state device logic on/off
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


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Oxygen'))
    myapp = MyWin()
    child_window = Child()
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
    # event slots children windows
    child_window.ui.pushButton.clicked.connect(myapp.Save_change)
    myapp.show()
    sys.exit(app.exec_())