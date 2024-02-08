# -*- coding: utf-8 -*-
# $Id: devices/d1281.py | Rev 42  | 2019/01/10 07:31:01 clu_wrk $
# xDevs.com Datron 1281 module
# Copyright (c) 2012-2019, xDevs.com
# 
# Python 2.7 | RPi3 
# Project maintainers:
#  o Tsemenko Ilya  (@)
# https://xdevs.com/guide/teckit
#
import os.path
import sys
import time
import numbers
import signal
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
else:
    print ("No interface defined!")
    quit()

cnt = 0
tread = 20
temp = 18

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

acmeas = 0
gfreq = 0
acstats = 0

class avms():
    temp = 38.5
    data = ""
    status_flag = 1
    temp_status_flag = 1

    def __init__(self,gpib,reflevel,name):
        self.gpib = gpib
        print ("\033[3;5H \033[0;33mGPIB[\033[1m%2d\033[0;33m] : Fluke 5790A/3\033[0;39m" % self.gpib)
        if cfg.get('teckit', 'interface') == 'gpib':
            self.inst = Gpib.Gpib(0, self.gpib, timeout = 180) # GPIB link
        elif cfg.get('teckit', 'interface') == 'vxi':
            self.inst = vxi11.Instrument(cfg.get('teckit', 'dcc_ip'), "gpib0,%d" % self.gpib) # VXI link
            self.inst.timeout = 600
        self.reflevel = reflevel
        self.name = name
        self.init_inst_dummy()

    def init_inst_fres(self):
        # Setup SCPI DMM
        self.inst.clear()
        self.inst.write("*RST")
        self.inst.write("*CLR")
        self.inst.write(":SYST:AZER:TYPE SYNC")
        self.inst.write(":SYST:LSYN:STAT ON")
        self.inst.write(":SENS:FUNC 'FRES'")
        self.inst.write(":SENS:FRES:DIG 9;NPLC 30;AVER:COUN 10;TCON MOV")
        self.inst.write(":SENS:FRES:AVER:STAT ON")
        self.inst.write(":SENS:FRES:OCOM ON")
        self.inst.write(":SENS:FRES:RANG 20E3")
        self.inst.write(":FORM:ELEM READ")

    def init_inst_dummy(self):
        # Setup SCPI DMM
        self.inst.write("EXTGUARD ON")
        self.inst.write("HIRES ON")
        time.sleep(0.1)

    def init_inst(self):
        # Setup SCPI DMM
        self.inst.clear()
        self.inst.write("*RST")
        self.inst.write("*CLR")
        self.inst.write("RMS FILT10HZ")
        #self.inst.write("GUARD EXT")
#        #kei.write("READ?")

    def set_acv_range(self,cmd):
        # Setup SCPI DMM
        self.inst.write("RANGE AUTO")
        self.inst.write("RANGE %.4f" % cmd)
        self.inst.write("RANGE LOCK")

    def set_aci_range(self,cmd):
        # Setup SCPI DMM
        self.inst.write("RANGE AUTO")
        self.inst.write("RANGE %.4f" % cmd)
        self.inst.write("RANGE LOCK")

    def set_input(self,cmd):
        # Setup SCPI DMM
        self.inst.write("INPUT %s" % cmd)

    def set_dcv_fast_range(self,cmd):
        # Setup SCPI DMM
        self.inst.write("DCV %.3f,FILT_OFF,RESL8,FAST_ON" % cmd)

    def read_data(self,cmd):
        data_float = 0.0
        data_str = ""
        valstr = 0
        global gfreq
        global acmeas
        global acstats
        self.inst.write(cmd)
        try:
            with Timeout(300):
                data_str = self.inst.read()
        except Timeout.Timeout:
            print ("\033[40;103H Timeout exception from dmm %s on read_data() inst.read()\n" % self.name)
            return (0,float(0))
        print ("\033[40;103H 5790:  %s = %s" % (self.name,data_str))
        valstr = data_str.split(",")[0]
        acmeas = float(valstr)
        gfreq  = float(data_str.split(",")[1])
        acstats  = float(data_str.split(",")[2])
        try:
            data_float = float(valstr)
        except ValueError:
            print("\033[6;36HException %s on read_data(), ValueError = %s\n" % (self.name,data_str))
            return (0,float(0)) # Exception on float conversion, 0 = error
        #print data_str
        return (1,data_float) # Good read, 1 = converted to float w/o exception

    def trigger_ac(self):
        self.inst.write("TRIG")

    def get_data(self):
        #print self.data
        self.status_flag,data = self.read_data("*WAI;VAL?")
        if (self.status_flag):
            self.data = data#(data - 0.75) / 0.01 # Preamp A = 1000
        return self.data

    def get_freq(self):
        global gfreq
        global acstats
        return gfreq, acstats

    def get_acvm_values(self):
        global acmeas
        global gfreq
        global acstats
        self.status_flag,data = self.read_data("*WAI;VAL?")
        return acmeas, gfreq, acstats

    def get_data_status(self):
        return self.status_flag

