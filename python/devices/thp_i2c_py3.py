# -*- coding: utf-8 -*-
# $Id: devices/thp_i2c_py3.py | Rev 61  | 2022/08/05 03:46:12 tin_fpga $
# xDevs.com BME280 THP module
# Copyright (c) 2012-2019, xDevs.com
# 
# Python 3.x | RPi3 
# Project maintainers:
#  o Tsemenko Ilya  (@)
# https://xdevs.com/guide/teckit
#
import os.path
import sys
import time
import ftplib
import numbers
import signal
import smbus2
import bme280
import six
if six.PY2:
    import ConfigParser as ConfigParser
    cfg = ConfigParser.ConfigParser()
else:
    import configparser
    cfg = configparser.ConfigParser(inline_comment_prefixes=(';','#',))

cfg.read('teckit.conf')
cfg.sections()

if cfg.get('teckit', 'interface') == 'gpib':
    import Gpib
elif cfg.get('teckit', 'interface') == 'vxi':
    import vxi11
elif cfg.get('teckit', 'interface') == 'visa':
    import visa
    rm = visa.ResourceManager()
else:
    print ("No interface defined!")
    quit()

port = 1
address = 0x77
bus = smbus2.SMBus(port)
calibration_params = bme280.load_calibration_params(bus, address)

class Timeout():
  """Timeout class using ALARM signal"""
  class Timeout(Exception): pass

  def __init__(self, sec):
    self.sec = sec

  def __enter__(self):
    signal.signal(signal.SIGALRM, self.raise_timeout)
    signal.alarm(self.sec)

  def __exit__(self, *args):
    signal.alarm(0) # disable alarm

  def raise_timeout(self, *args):
    raise Timeout.Timeout()

class thp_meter():
    temp = 38.5
    data = ""
    ppm = 0.0
    status_flag = 1
    temp_status_flag = 1
    global exttemp
    global rh
    global hectopascals
    global tec_rtd
    global calibration_params

    def __init__(self,gpib,reflevel,name):
        self.gpib = gpib
        print ("\033[1;5H \033[0;33mI2C[\033[1m%2d\033[0;33m] : BME280\033[0;39m" % 0x77)
        self.name = name

    def getTHP(self):
        global calibration_params
        error = 0
        data = bme280.sample(bus, address, calibration_params)
        self.exttemp = data.temperature
        self.rh = data.humidity
        self.press = data.pressure
        return (error,self.exttemp,self.rh,self.press)

