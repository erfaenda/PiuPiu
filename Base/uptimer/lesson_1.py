# -*- coding: utf-8 -*-
from datetime import timedelta

def uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
        #print(uptime_string)
        my_file = open('uplog.txt', 'w')
        text_for_file = uptime_string
        my_file.write(text_for_file)

        my_file.close()
uptime()