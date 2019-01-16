#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

import serial, time
import datetime
from serial import SerialException

class Gps_time():
    def __init__(self):
        self.set_date = ""
        self.set_time = ""
    def get_time(self):
        try:
            self.gps = serial.Serial('/tty/USB0', 4800, timeout=1)
        except:
            return "ERROR"     
        while(1):
            response = self.gps.readline().decode('ascii')     							# read up to return data 30 bytes (timeout)
#            print(response)
            if (response.split(',')[0] == "$GPRMC"):
                date = datetime.datetime.strptime(response.split(',')[9], '%d%m%y')
#                print("DATE : ", date.year, date.month, date.day)
                self.set_date = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
#                print(set_date)
            if (response.split(',')[0] == "$GPGGA"):
                now = datetime.datetime.strptime(response.split(',')[1].split('.')[0], '%I%M%S')
#                print("Now", now.hour+ 8, now.minute, now.second)
                self.set_time = str(now.hour+ 8) + ":" + str(now.minute) + ":" + str(now.second)
#                print(set_time)
            if (self.set_time != "" and self.set_date != ""):
#               print("set GPS time")
                print('sudo date -s "' + self.set_date + ' ' + self.set_time + '"')
                break
        self.gps.close()

Gps_time()