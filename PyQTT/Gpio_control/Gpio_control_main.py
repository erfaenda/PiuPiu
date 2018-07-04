#! /usr/bin/env python
# -*- coding: utf-8 -*-

#import RPi.GPIO as GPIO
import sys, time, os, configparser, threading
from datetime import timedelta, datetime
from PyQTT.Gpio_control.gpio_gui import *
from PyQTT.Gpio_control.gpio_child import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QStyleFactory, QToolTip

# Тестирую второй поток на бесконечном цыкле
class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        i = 0
        while True:
            print('Test ' + str(i))
            i = i + 1
            time.sleep(0.3)
            if i == 10:
                print('finish')
                break
    def Opros(self):
        i = 0
        while True:
            print('Test ' + str(i))
            i = i + 1
            time.sleep(0.3)
            if i == 10:
                print('finish')
                break





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
    list_checkboxes_device_logic = []

    # devices value
    list_devices = ['Средняя температура', 'Температура 1','Температура 2','Гигрометр 1','Гигрометр 2',
                    'Средняя влажность ']
    temp_1 = 0
    temp_2 = 0
    middle_temp = 0
    gigro_1 = 0
    gigro_2 = 0
    middle_humidity = 0
    unknow_1 = 0
    unknow_2 = 0

    # Logic state value
    deviceLogic_state = 0
    timeLogic_state = 0

    # logic value
    globalTime = 0
    spin_min = 0
    spin_max = 0
    dev_min = 0
    dev_max = 0

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.uptime()
        self.append_list_checkboxes()
        self.ui.buttonGroup.setExclusive(False)
        self.setWindowIcon(QIcon('ico.png'))
        # signals and slots
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
        self.ui.action_2.triggered.connect(self.save_config)
        self.ui.action.triggered.connect(self.close)


    # switch on
    def sw_on(self, sw_state):
        if self.list_state[sw_state] == False:
            self.list_state[sw_state] = True
    # switch off
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
        if self.timeLogic_state == 1:
            time_min = self.ui.timeEdit.time()
            time_max = self.ui.timeEdit_2.time()
            now = datetime.now()
            self.spin_min = now.replace(hour=time_min.hour(), minute=time_min.minute(), second=0, microsecond=0)
            self.spin_max = now.replace(hour=time_max.hour(), minute=time_max.minute(), second=0, microsecond=0)
            # off range
            if now >= self.spin_min and now <= self.spin_max:
                self.sw1_off()
            else:
                self.sw1_on()

    # universal main fuction read time and control gpio ports
    def uni_timer_logic(self, time_min, time_max, sw_state, checkbox_in_list, combobox):
        if self.timeLogic_state == 1:
            if self.list_checkboxes_time_logic[checkbox_in_list].isChecked():
                now = datetime.now()
                self.spin_min = now.replace(hour=time_min.hour(), minute=time_min.minute(), second=0,
                                            microsecond=0)
                self.spin_max = now.replace(hour=time_max.hour(), minute=time_max.minute(), second=0,
                                            microsecond=0)
                # off range and on range
                if combobox.currentIndex() == 1:
                    if now >= self.spin_min and now <= self.spin_max:
                        self.list_state[sw_state] = False
                    else:
                        self.list_state[sw_state] = True
                else:
                    if now >= self.spin_min and now <= self.spin_max:
                        self.list_state[sw_state] = True
                    else:
                        self.list_state[sw_state] = False
        return

    # control gpio ports in device block
    # тоже неправильно, но пока пусть будет так...
    def uni_device_logic(self, min, max, sw_state, checkbox_in_list, combobox):
        if self.deviceLogic_state == 1:
            if self.list_checkboxes_device_logic[checkbox_in_list].isChecked():
                if combobox.currentIndex() == 0:
                    if self.middle_temp < min:
                        self.list_state[sw_state] = True
                    if self.middle_temp > max:
                        self.list_state[sw_state] = False
                if combobox.currentIndex() == 1:
                    if self.temp_1 < min:
                        self.list_state[sw_state] = True
                    if self.temp_1 > max:
                        self.list_state[sw_state] = False
                if combobox.currentIndex() == 2:
                    if self.temp_2 < min:
                        self.list_state[sw_state] = True
                    if self.temp_2 > max:
                        self.list_state[sw_state] = False
                if combobox.currentIndex() == 3:
                    if self.gigro_1 < min:
                        self.list_state[sw_state] = True
                    if self.gigro_1 > max:
                        self.list_state[sw_state] = False
                if combobox.currentIndex() == 4:
                    if self.gigro_2 < min:
                        self.list_state[sw_state] = True
                    if self.gigro_2 > max:
                        self.list_state[sw_state] = False
                if combobox.currentIndex() == 5:
                    if self.middle_humidity < min:
                        self.list_state[sw_state] = True
                    if self.middle_humidity > max:
                        self.list_state[sw_state] = False
                if combobox.currentIndex() == 6:
                    if self.unknow_1 < min:
                        self.list_state[sw_state] = True
                    if self.unknow_1 > max:
                        self.list_state[sw_state] = False
                if combobox.currentIndex() == 7:
                    if self.unknow_2 < min:
                        self.list_state[sw_state] = True
                    if self.unknow_2 > max:
                        self.list_state[sw_state] = False

    # add obj checkboxes in lists
    def append_list_checkboxes(self):
        for i in range(1,9):
            str_1 = 'checkBox_time_logic_{}'.format(i)
            str_2 = 'checkBox_device_logic_{}'.format(i)
            abstract_chkbx = self.findChild(QtCore.QObject, str_1)
            abstract_chkbx_2 = self.findChild(QtCore.QObject, str_2)
            self.list_checkboxes_time_logic.append(abstract_chkbx)
            self.list_checkboxes_device_logic.append(abstract_chkbx_2)
    # add tooltips
    def add_tooltips(self, combobox):
        if combobox.currentIndex() == 2:
            combobox.setToolTip('ХАХАХАХ')



    # function starter
    def starter_all_timer_logic(self):
        self.uni_timer_logic(self.ui.timeEdit.time(), self.ui.timeEdit_2.time(), 0, 0, self.ui.comboBox)
        self.uni_timer_logic(self.ui.timeEdit_3.time(), self.ui.timeEdit_4.time(), 1, 1, self.ui.comboBox_2)
        self.uni_timer_logic(self.ui.timeEdit_7.time(), self.ui.timeEdit_8.time(), 2, 2, self.ui.comboBox_3)
        self.uni_timer_logic(self.ui.timeEdit_5.time(), self.ui.timeEdit_6.time(), 3, 3, self.ui.comboBox_4)
        self.uni_timer_logic(self.ui.timeEdit_18.time(), self.ui.timeEdit_17.time(), 4, 4, self.ui.comboBox_5)
        self.uni_timer_logic(self.ui.timeEdit_20.time(), self.ui.timeEdit_19.time(), 5, 5, self.ui.comboBox_6)
        self.uni_timer_logic(self.ui.timeEdit_24.time(), self.ui.timeEdit_23.time(), 6, 6, self.ui.comboBox_7)
        self.uni_timer_logic(self.ui.timeEdit_26.time(), self.ui.timeEdit_25.time(), 7, 7, self.ui.comboBox_8)
        # devices
        self.uni_device_logic(self.ui.spinBoxOn_logic_1.value(), self.ui.spinBoxOff_logic_1.value(), 0, 0, self.ui.comboBox_9)
        self.uni_device_logic(self.ui.spinBoxOn_logic_2.value(), self.ui.spinBoxOff_logic_2.value(), 1, 1, self.ui.comboBox_10)
        self.uni_device_logic(self.ui.spinBoxOn_logic_3.value(), self.ui.spinBoxOff_logic_3.value(), 2, 2, self.ui.comboBox_11)
        self.uni_device_logic(self.ui.spinBoxOn_logic_4.value(), self.ui.spinBoxOff_logic_4.value(), 3, 3, self.ui.comboBox_12)
        self.uni_device_logic(self.ui.spinBoxOn_logic_5.value(), self.ui.spinBoxOff_logic_5.value(), 4, 4, self.ui.comboBox_13)
        self.uni_device_logic(self.ui.spinBoxOn_logic_6.value(), self.ui.spinBoxOff_logic_6.value(), 5, 5, self.ui.comboBox_14)
        self.uni_device_logic(self.ui.spinBoxOn_logic_7.value(), self.ui.spinBoxOff_logic_7.value(), 6, 6, self.ui.comboBox_15)
        self.uni_device_logic(self.ui.spinBoxOn_logic_8.value(), self.ui.spinBoxOff_logic_8.value(), 7, 7, self.ui.comboBox_16)
        self.add_tooltips(self.ui.comboBox_9)

    # main function read devices value and control gpio ports
    def deviceLogic(self):
        if self.deviceLogic_state == 1:
            if self.middle_temp < self.ui.spinBoxOn_logic_1.value():
                self.sw_on(0)
            if self.middle_temp > self.ui.spinBoxOff_logic_1.value():
                self.sw_off(0)

    def switch_light(self):
        a = self.ui.timeEdit.time()
        #print(a.hour() + a.minute())

    # read devices values and show they, test func
    def readDevices(self):
        self.temp_1 = int(self.ui.temp1.text())
        self.temp_2 = int(self.ui.temp2.text())
        self.middle_temp = (self.temp_1 + self.temp_2) / 2
        self.ui.midtemp.setValue(self.middle_temp)

        self.gigro_1 = int(self.ui.gigro_1.text())
        self.gigro_2 = int(self.ui.gigro_2.text())
        self.middle_humidity = (self.gigro_1 + self.gigro_2) / 2
        self.ui.middle_hymanity.setValue(self.middle_humidity)

    # temp raspberry
    def measure_temp(self):
        temp = os.popen("vcgencmd measure_temp").readline()
        a = temp.replace("temp=", "")
        s = a[0:2]
        i = int(s)
        self.ui.midtemp.setValue(i)

    # time display only
    def dateTime(self):
        # display time
        now = datetime.strftime(datetime.now(), "%H:%M:%S")
        self.ui.label_6.setText('Системное время: ' + str(now))
        time = datetime.now()
        #print('time ' + str(self.globalTime))
        #print(self.list_state[0])

    # uptme system
    def uptime(self):
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds=uptime_seconds))

        self.ui.label.setText(uptime_string)

        # тут надо переписать как то модно
    '''def check_state_2(self):
        for state in self.list_state:
            if state == False:'''

    # check state ports and switch real gpio ports
    def check_state(self):
        # check state buttons on/off
        # это гавно надо переписать
        if self.list_state[0] == False:
            self.ui.label_status_port1.setText('OFF')
            self.ui.pushButton.setStyleSheet("""
                                   QPushButton {
                                       background: rgba(255, 92, 16, 100);
                                   }
                                   """)
            self.ui.label_status_port1.setStyleSheet("""
                                    QLabel {
                                        background: rgba(255, 92, 16, 30);
                                    }
                                    """)
            #GPIO.setup(4, GPIO.IN)

        else:
            self.ui.label_status_port1.setText('ON')
            self.ui.pushButton.setStyleSheet("""
                       QPushButton {
                           background: rgba(25, 188, 50, 145);
                       }
                       """)
            self.ui.label_status_port1.setStyleSheet("""
                        QLabel {
                            background: rgba(25, 188, 50, 145);
                        }
                        """)
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
        if self.deviceLogic_state == 0:
            self.ui.label__status_logic.setText('Logic disable')
        else:
            self.ui.label__status_logic.setText('Logic enable')

        if self.timeLogic_state == 0:
            self.ui.label_time_status.setText('Logic disable')
        else:
            self.ui.label_time_status.setText('Logic enable')

    def device_logicON(self):
        self.deviceLogic_state = 1

        print(self.deviceLogic_state)

    def device_logicOFF(self):
        self.deviceLogic_state = 0
        print(self.deviceLogic_state)

    def time_logicON(self):
        self.timeLogic_state = 1

    def time_logicOFF(self):
        self.timeLogic_state = 0

    # датчики виснут в опросе а отдельный поток создавать я пока не умею
    # по этому я буду опрашивать их отдельным скриптом, а отсюда парсить
    def read_dht22_down(self):
        config = configparser.ConfigParser()
        config.read("/home/pi/Templates/Gpio_control/DHT.ini")

        # Читаем некоторые значения из конфиг. файла.
        t = config.get("DHT22_last", "temperature")
        h = config.get("DHT22_last", "humi")

    # более чем позорный код
    def read_config(self):
        path = "settings.ini"
        self.readConfig(path)

    def save_config(self):
        path = "settings.ini"
        self.createConfig(path)

    # create config file
    # Когданибудь я это перепишу
    def createConfig(self, path):
        # Create a config file
        config = configparser.ConfigParser()
        config.add_section("Settings")

        config.set("Settings", "device_logic", str(self.deviceLogic_state))
        config.set("Settings", "time_logic", str(self.timeLogic_state))

        config.set("Settings", "port_name_1", str(child_window.ui.lineEdit_1.text()))
        config.set("Settings", "port_name_2", str(child_window.ui.lineEdit_2.text()))
        config.set("Settings", "port_name_3", str(child_window.ui.lineEdit_3.text()))
        config.set("Settings", "port_name_4", str(child_window.ui.lineEdit_4.text()))
        config.set("Settings", "port_name_5", str(child_window.ui.lineEdit_5.text()))
        config.set("Settings", "port_name_6", str(child_window.ui.lineEdit_6.text()))
        config.set("Settings", "port_name_7", str(child_window.ui.lineEdit_7.text()))
        config.set("Settings", "port_name_8", str(child_window.ui.lineEdit_8.text()))
        # time logic
        config.set("Settings", "time_box_1", str(self.ui.comboBox.currentIndex()))
        config.set("Settings", "time_box_2", str(self.ui.comboBox_2.currentIndex()))
        config.set("Settings", "time_box_3", str(self.ui.comboBox_3.currentIndex()))
        config.set("Settings", "time_box_4", str(self.ui.comboBox_4.currentIndex()))
        config.set("Settings", "time_box_5", str(self.ui.comboBox_5.currentIndex()))
        config.set("Settings", "time_box_6", str(self.ui.comboBox_6.currentIndex()))
        config.set("Settings", "time_box_7", str(self.ui.comboBox_7.currentIndex()))
        config.set("Settings", "time_box_8", str(self.ui.comboBox_8.currentIndex()))

        config.set("Settings", "time_spin_min_1", self.ui.timeEdit.text())
        config.set("Settings", "time_spin_min_2", self.ui.timeEdit_3.text())
        config.set("Settings", "time_spin_min_3", self.ui.timeEdit_7.text())
        config.set("Settings", "time_spin_min_4", self.ui.timeEdit_5.text())
        config.set("Settings", "time_spin_min_5", self.ui.timeEdit_18.text())
        config.set("Settings", "time_spin_min_6", self.ui.timeEdit_20.text())
        config.set("Settings", "time_spin_min_7", self.ui.timeEdit_24.text())
        config.set("Settings", "time_spin_min_8", self.ui.timeEdit_26.text())

        config.set("Settings", "time_spin_max_1", self.ui.timeEdit_2.text())
        config.set("Settings", "time_spin_max_2", self.ui.timeEdit_4.text())
        config.set("Settings", "time_spin_max_3", self.ui.timeEdit_8.text())
        config.set("Settings", "time_spin_max_4", self.ui.timeEdit_6.text())
        config.set("Settings", "time_spin_max_5", self.ui.timeEdit_17.text())
        config.set("Settings", "time_spin_max_6", self.ui.timeEdit_19.text())
        config.set("Settings", "time_spin_max_7", self.ui.timeEdit_23.text())
        config.set("Settings", "time_spin_max_8", self.ui.timeEdit_25.text())

        for chk in range(0, 8):
            if self.list_checkboxes_time_logic[chk].isChecked() == True:
                config.set("Settings", "time_checkbox_{}".format(chk+1), "1")
            else:
                config.set("Settings", "time_checkbox_{}".format(chk+1), "0")

        # device logic
        config.set("Settings", "dev_box_1", str(self.ui.comboBox_9.currentIndex()))
        config.set("Settings", "dev_box_2", str(self.ui.comboBox_10.currentIndex()))
        config.set("Settings", "dev_box_3", str(self.ui.comboBox_11.currentIndex()))
        config.set("Settings", "dev_box_4", str(self.ui.comboBox_12.currentIndex()))
        config.set("Settings", "dev_box_5", str(self.ui.comboBox_13.currentIndex()))
        config.set("Settings", "dev_box_6", str(self.ui.comboBox_14.currentIndex()))
        config.set("Settings", "dev_box_7", str(self.ui.comboBox_15.currentIndex()))
        config.set("Settings", "dev_box_8", str(self.ui.comboBox_16.currentIndex()))

        config.set("Settings", "dev_spin_min_1", str(self.ui.spinBoxOn_logic_1.value()))
        config.set("Settings", "dev_spin_min_2", str(self.ui.spinBoxOn_logic_2.value()))
        config.set("Settings", "dev_spin_min_3", str(self.ui.spinBoxOn_logic_3.value()))
        config.set("Settings", "dev_spin_min_4", str(self.ui.spinBoxOn_logic_4.value()))
        config.set("Settings", "dev_spin_min_5", str(self.ui.spinBoxOn_logic_5.value()))
        config.set("Settings", "dev_spin_min_6", str(self.ui.spinBoxOn_logic_6.value()))
        config.set("Settings", "dev_spin_min_7", str(self.ui.spinBoxOn_logic_7.value()))
        config.set("Settings", "dev_spin_min_8", str(self.ui.spinBoxOn_logic_8.value()))

        config.set("Settings", "dev_spin_max_1", str(self.ui.spinBoxOff_logic_1.value()))
        config.set("Settings", "dev_spin_max_2", str(self.ui.spinBoxOff_logic_2.value()))
        config.set("Settings", "dev_spin_max_3", str(self.ui.spinBoxOff_logic_3.value()))
        config.set("Settings", "dev_spin_max_4", str(self.ui.spinBoxOff_logic_4.value()))
        config.set("Settings", "dev_spin_max_5", str(self.ui.spinBoxOff_logic_5.value()))
        config.set("Settings", "dev_spin_max_6", str(self.ui.spinBoxOff_logic_6.value()))
        config.set("Settings", "dev_spin_max_7", str(self.ui.spinBoxOff_logic_7.value()))
        config.set("Settings", "dev_spin_max_8", str(self.ui.spinBoxOff_logic_8.value()))

        # сохраняю состояние чекбоксов
        for chk in range(0, 8):
            if self.list_checkboxes_device_logic[chk].isChecked() == True:
                config.set("Settings", "dev_checkbox_{}".format(chk+1), "1")
            else:
                config.set("Settings", "dev_checkbox_{}".format(chk+1), "0")


        '''config.set("Settings", "dev_checkbox_1", "0")
        config.set("Settings", "dev_checkbox_2", "0")
        config.set("Settings", "dev_checkbox_3", "0")
        config.set("Settings", "dev_checkbox_4", "0")
        config.set("Settings", "dev_checkbox_5", "0")
        config.set("Settings", "dev_checkbox_6", "0")
        config.set("Settings", "dev_checkbox_7", "0")
        config.set("Settings", "dev_checkbox_8", "0")'''

        with open(path, "w") as config_file:
            config.write(config_file)

    def readConfig(self, path):

        """
        Create, read, update, delete config
        """
        if not os.path.exists(path):
            self.createConfig(path)

        config = configparser.ConfigParser()
        config.read(path)

        '''if config.get("Settings", "time_logic") == False:
            self.timeLogic_state = 0
        else:
            self.timeLogic_state = 1'''
        self.timeLogic_state = int(config.get("Settings", "time_logic"))
        self.deviceLogic_state = int(config.get("Settings", "device_logic"))

        # Читаем некоторые значения из конфиг. файла.
        # названия портов
        child_window.ui.lineEdit_1.setText(config.get("Settings", "port_name_1"))
        child_window.ui.lineEdit_2.setText(config.get("Settings", "port_name_2"))
        child_window.ui.lineEdit_3.setText(config.get("Settings", "port_name_3"))
        child_window.ui.lineEdit_4.setText(config.get("Settings", "port_name_4"))
        child_window.ui.lineEdit_5.setText(config.get("Settings", "port_name_5"))
        child_window.ui.lineEdit_6.setText(config.get("Settings", "port_name_6"))
        child_window.ui.lineEdit_7.setText(config.get("Settings", "port_name_7"))
        child_window.ui.lineEdit_8.setText(config.get("Settings", "port_name_8"))
        # индексы комбобоксов
        self.ui.comboBox.setCurrentIndex(int(config.get("Settings", "time_box_1")))
        self.ui.comboBox_2.setCurrentIndex(int(config.get("Settings", "time_box_2")))
        self.ui.comboBox_3.setCurrentIndex(int(config.get("Settings", "time_box_3")))
        self.ui.comboBox_4.setCurrentIndex(int(config.get("Settings", "time_box_4")))
        self.ui.comboBox_5.setCurrentIndex(int(config.get("Settings", "time_box_5")))
        self.ui.comboBox_6.setCurrentIndex(int(config.get("Settings", "time_box_6")))
        self.ui.comboBox_7.setCurrentIndex(int(config.get("Settings", "time_box_7")))
        self.ui.comboBox_8.setCurrentIndex(int(config.get("Settings", "time_box_8")))

        self.ui.comboBox_9.setCurrentIndex(int(config.get("Settings", "dev_box_1")))
        self.ui.comboBox_10.setCurrentIndex(int(config.get("Settings", "dev_box_2")))
        self.ui.comboBox_11.setCurrentIndex(int(config.get("Settings", "dev_box_3")))
        self.ui.comboBox_12.setCurrentIndex(int(config.get("Settings", "dev_box_4")))
        self.ui.comboBox_13.setCurrentIndex(int(config.get("Settings", "dev_box_5")))
        self.ui.comboBox_14.setCurrentIndex(int(config.get("Settings", "dev_box_6")))
        self.ui.comboBox_15.setCurrentIndex(int(config.get("Settings", "dev_box_7")))
        self.ui.comboBox_16.setCurrentIndex(int(config.get("Settings", "dev_box_8")))

        list_time_text_spin = []
        list_int_time_spin = []
        # забираю текстовое значение из спинов и забиваю ими список
        list_time_text_spin.append(config.get("Settings", "time_spin_min_1"))
        list_time_text_spin.append(config.get("Settings", "time_spin_min_2"))
        list_time_text_spin.append(config.get("Settings", "time_spin_min_3"))
        list_time_text_spin.append(config.get("Settings", "time_spin_min_4"))
        list_time_text_spin.append(config.get("Settings", "time_spin_min_5"))
        list_time_text_spin.append(config.get("Settings", "time_spin_min_6"))
        list_time_text_spin.append(config.get("Settings", "time_spin_min_7"))
        list_time_text_spin.append(config.get("Settings", "time_spin_min_8"))

        list_time_text_spin.append(config.get("Settings", "time_spin_max_1"))
        list_time_text_spin.append(config.get("Settings", "time_spin_max_2"))
        list_time_text_spin.append(config.get("Settings", "time_spin_max_3"))
        list_time_text_spin.append(config.get("Settings", "time_spin_max_4"))
        list_time_text_spin.append(config.get("Settings", "time_spin_max_5"))
        list_time_text_spin.append(config.get("Settings", "time_spin_max_6"))
        list_time_text_spin.append(config.get("Settings", "time_spin_max_7"))
        list_time_text_spin.append(config.get("Settings", "time_spin_max_8"))

        # разбираю строку на минуты и часы, конвертирую и снова забиваю список, тупо....
        for text in list_time_text_spin:
            index = text.find(":")
            hour = text[:index]
            minute = text[index + 1:]
            hour = int(hour)
            minute = int(minute)
            list_int_time_spin.append(hour)
            list_int_time_spin.append(minute)
            print(list_int_time_spin)

        # раз уж я тупо забил список, так же тупо подставлю значения из списка в спин при загрузке
        self.ui.timeEdit.setTime(QtCore.QTime(list_int_time_spin[0], list_int_time_spin[1]))
        self.ui.timeEdit_3.setTime(QtCore.QTime(list_int_time_spin[2], list_int_time_spin[3]))
        self.ui.timeEdit_7.setTime(QtCore.QTime(list_int_time_spin[4], list_int_time_spin[5]))
        self.ui.timeEdit_5.setTime(QtCore.QTime(list_int_time_spin[6], list_int_time_spin[7]))
        self.ui.timeEdit_18.setTime(QtCore.QTime(list_int_time_spin[8], list_int_time_spin[9]))
        self.ui.timeEdit_20.setTime(QtCore.QTime(list_int_time_spin[10], list_int_time_spin[11]))
        self.ui.timeEdit_24.setTime(QtCore.QTime(list_int_time_spin[12], list_int_time_spin[13]))
        self.ui.timeEdit_26.setTime(QtCore.QTime(list_int_time_spin[14], list_int_time_spin[15]))

        self.ui.timeEdit_2.setTime(QtCore.QTime(list_int_time_spin[16], list_int_time_spin[17]))
        self.ui.timeEdit_4.setTime(QtCore.QTime(list_int_time_spin[18], list_int_time_spin[19]))
        self.ui.timeEdit_8.setTime(QtCore.QTime(list_int_time_spin[20], list_int_time_spin[21]))
        self.ui.timeEdit_6.setTime(QtCore.QTime(list_int_time_spin[22], list_int_time_spin[23]))
        self.ui.timeEdit_17.setTime(QtCore.QTime(list_int_time_spin[24], list_int_time_spin[25]))
        self.ui.timeEdit_19.setTime(QtCore.QTime(list_int_time_spin[26], list_int_time_spin[27]))
        self.ui.timeEdit_23.setTime(QtCore.QTime(list_int_time_spin[28], list_int_time_spin[29]))
        self.ui.timeEdit_25.setTime(QtCore.QTime(list_int_time_spin[30], list_int_time_spin[31]))

        # рапихиваю числовые спины
        self.ui.spinBoxOn_logic_1.setValue(int(config.get("Settings", "dev_spin_min_1")))
        self.ui.spinBoxOn_logic_2.setValue(int(config.get("Settings", "dev_spin_min_2")))
        self.ui.spinBoxOn_logic_3.setValue(int(config.get("Settings", "dev_spin_min_3")))
        self.ui.spinBoxOn_logic_4.setValue(int(config.get("Settings", "dev_spin_min_4")))
        self.ui.spinBoxOn_logic_5.setValue(int(config.get("Settings", "dev_spin_min_5")))
        self.ui.spinBoxOn_logic_6.setValue(int(config.get("Settings", "dev_spin_min_6")))
        self.ui.spinBoxOn_logic_7.setValue(int(config.get("Settings", "dev_spin_min_7")))
        self.ui.spinBoxOn_logic_8.setValue(int(config.get("Settings", "dev_spin_min_8")))

        self.ui.spinBoxOff_logic_1.setValue(int(config.get("Settings", "dev_spin_max_1")))
        self.ui.spinBoxOff_logic_2.setValue(int(config.get("Settings", "dev_spin_max_2")))
        self.ui.spinBoxOff_logic_3.setValue(int(config.get("Settings", "dev_spin_max_3")))
        self.ui.spinBoxOff_logic_4.setValue(int(config.get("Settings", "dev_spin_max_4")))
        self.ui.spinBoxOff_logic_5.setValue(int(config.get("Settings", "dev_spin_max_5")))
        self.ui.spinBoxOff_logic_6.setValue(int(config.get("Settings", "dev_spin_max_6")))
        self.ui.spinBoxOff_logic_7.setValue(int(config.get("Settings", "dev_spin_max_7")))
        self.ui.spinBoxOff_logic_8.setValue(int(config.get("Settings", "dev_spin_max_8")))

        # расставляем чекбоксы
        self.ui.checkBox_time_logic_1.setChecked(int(config.get("Settings", "time_checkbox_1")))
        self.ui.checkBox_time_logic_2.setChecked(int(config.get("Settings", "time_checkbox_2")))
        self.ui.checkBox_time_logic_3.setChecked(int(config.get("Settings", "time_checkbox_3")))
        self.ui.checkBox_time_logic_4.setChecked(int(config.get("Settings", "time_checkbox_4")))
        self.ui.checkBox_time_logic_5.setChecked(int(config.get("Settings", "time_checkbox_5")))
        self.ui.checkBox_time_logic_6.setChecked(int(config.get("Settings", "time_checkbox_6")))
        self.ui.checkBox_time_logic_7.setChecked(int(config.get("Settings", "time_checkbox_7")))
        self.ui.checkBox_time_logic_8.setChecked(int(config.get("Settings", "time_checkbox_8")))

        self.ui.checkBox_device_logic_1.setChecked(int(config.get("Settings", "dev_checkbox_1")))
        self.ui.checkBox_device_logic_2.setChecked(int(config.get("Settings", "dev_checkbox_2")))
        self.ui.checkBox_device_logic_3.setChecked(int(config.get("Settings", "dev_checkbox_3")))
        self.ui.checkBox_device_logic_4.setChecked(int(config.get("Settings", "dev_checkbox_4")))
        self.ui.checkBox_device_logic_5.setChecked(int(config.get("Settings", "dev_checkbox_5")))
        self.ui.checkBox_device_logic_6.setChecked(int(config.get("Settings", "dev_checkbox_6")))
        self.ui.checkBox_device_logic_7.setChecked(int(config.get("Settings", "dev_checkbox_7")))
        self.ui.checkBox_device_logic_8.setChecked(int(config.get("Settings", "dev_checkbox_8")))

        self.Save_change()


if __name__=="__main__":
    t = threading.Thread(target=A)
    t.start()
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Oxygen'))
    myapp = MyWin()
    child_window = Child()
    path = "settings.ini"
    myapp.read_config()
    timer = QTimer()
    timer.timeout.connect(myapp.check_state)
    timer.start(100)
    timeing = QTimer()
    #timeing.timeout.connect(myapp.uptime)
    timeing.timeout.connect(myapp.dateTime)
    timeing.timeout.connect(myapp.switch_light)
    timeing.timeout.connect(myapp.readDevices)
    #timeing.timeout.connect(myapp.deviceLogic)
    #timeing.timeout.connect(myapp.timer_logic)
    timeing.timeout.connect(myapp.starter_all_timer_logic)
    timeing.start(1000)
    # event slots children windows
    child_window.ui.pushButton.clicked.connect(myapp.Save_change)
    myapp.show()
    sys.exit(app.exec_())