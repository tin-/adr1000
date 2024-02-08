# -*- coding: utf-8 -*-
# $Id: devices/k2002.py | Rev 63  | 2022/08/12 05:13:29 tin_fpga $
# xDevs.com Keithley 2002 module
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

cfg.read('../teckit2.conf')
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

class vm_meter():
    temp = 38.5
    data = ""
    status_flag = 1
    temp_status_flag = 1

    def __init__(self,gpib,reflevel,name):
        self.gpib = gpib
        print ("\033[5;5H \033[0;31mGPIB[\033[1m%2d\033[0;31m] : Keithley VM02\033[0;39m" % self.gpib)
        if cfg.get('teckit', 'interface') == 'gpib':
            self.inst = Gpib.Gpib(0, self.gpib, timeout = 180) # GPIB link
        elif cfg.get('teckit', 'interface') == 'vxi':
            self.inst = vxi11.Instrument(cfg.get('teckit', 'mfc_ip'), "gpib0,%d" % self.gpib) # VXI link
            self.inst.timeout = 2
        elif cfg.get('teckit', 'interface') == 'visa':
            self.inst = rm.open_resource('GPIB::%d::INSTR' % self.gpib)
            self.inst.timeout = 300000 # timeout delay in ms
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
        self.inst.write(":SENS:FRES:DIG 9;NPLC 20;AVER:COUN 10;TCON MOV")
        self.inst.write(":SENS:FRES:AVER:STAT ON")
        self.inst.write(":SENS:FRES:OCOM ON")
        self.inst.write(":SENS:FRES:RANG 20E3")
        self.inst.write(":FORM:ELEM READ")

    def init_inst_dummy(self):
        # Setup SCPI DMM
        #self.inst.write("i?")
        time.sleep(0.1)

    def init_inst(self):
        # Setup SCPI DMM
        self.inst.clear()
        self.inst.write("*RST")
        self.inst.write("*CLR")
        self.inst.write(":SYST:AZER:TYPE SYNC")
        self.inst.write(":SYST:LSYN:STAT ON")
        #self.inst.write(":SENS:FUNC 'TEMP'")
        #self.inst.write(":SENS:TEMP:DIG 7")
        #self.inst.write(":SENS:TEMP:NPLC 10")
        self.inst.write(":SENS:FUNC 'VOLT:DC'")
        self.inst.write(":SENS:VOLT:DC:DIG 9;NPLC 10;AVER:COUN 10;TCON MOV")
        self.inst.write(":SENS:VOLT:DC:AVER:STAT ON")
        self.inst.write(":SENS:VOLT:DC:RANG 20")
        self.inst.write(":FORM:ELEM READ")
#        self.inst.write(":DISP:WIND:TEXT:DATA \"               \";STAT ON;")
#        self.inst.write(":DISP:WIND2:TEXT:DATA \"               \";STAT ON;")
#        #kei.write("READ?")

    def set_pt1000_rtd(self):
        self.inst.write(":sens:temp:tran rtd")      #select thermistor
        self.inst.write(":sens:temp:rtd:type user") #10 kOhm thermistor
        self.inst.write(":sens:temp:rtd:alph 0.00375") #10 kOhm thermistor
        self.inst.write(":sens:temp:rtd:beta 0.160") #10 kOhm thermistor
        self.inst.write(":sens:temp:rtd:delt 1.605") #10 kOhm thermistor
        self.inst.write(":sens:temp:rtd:rzer 1000") #10 kOhm thermistor
        self.inst.write(":SENS:FUNC 'TEMP'")
        self.inst.write(":SENS:TEMP:DIG 7")
        self.inst.write(":SENS:TEMP:NPLC 10")

    def set_ohmf_range(self,cmd):
        # Setup SCPI DMM
        self.inst.write(":SENS:FUNC 'FRES'")
        self.inst.write(":SENS:FRES:DIG 9;NPLC 50;AVER:COUN 10;TCON MOV")
        if (float(cmd)) <= 21e3:
            self.inst.write(":SENS:FRES:OCOM ON")
        else:
            self.inst.write(":SENS:FRES:OCOM OFF")
        self.inst.write(":SENS:FRES:RANG %.2f" % cmd)

    def set_ohm_range(self,cmd):
        # Setup SCPI DMM
        self.inst.write(":SENS:FUNC 'RES'")
        self.inst.write(":SENS:RES:DIG 9;NPLC 50;AVER:COUN 10;TCON MOV")
        self.inst.write(":SENS:RES:OCOM OFF")
        self.inst.write(":SENS:RES:RANG %.2f" % cmd)

    def set_dcv_range(self,cmd):
        # Setup SCPI DMM
        self.inst.write(":SENS:FUNC 'VOLT:DC'")
        self.inst.write(":SENS:VOLT:DC:DIG 9;NPLC 20;RANG %.2f" % cmd)
        self.inst.write(":SENS:VOLT:DC:AVER:STAT ON")
        self.inst.write(":SENS:VOLT:DC:TCON MOV")

    def set_dci_range(self,cmd):
        # Setup SCPI DMM
        self.inst.write(":SENS:FUNC 'CURR:DC'")
        self.inst.write(":SENS:CURR:DC:DIG 9;NPLC 50;RANG %.2f" % cmd)

    def trigger(self):
        self.inst.write("READ?")

    def wrdat(self,cmd):
        self.inst.write(cmd)

    def read_val(self):
        data_float = 0.0
        data_str = ""
        try:
            with Timeout(1):
                data_str = self.inst.read()
        except Timeout.Timeout:
            print ("Timeout exception from dmm %s on read_data() inst.read()\n" % self.name)
            return (0,float(0))
        print (data_str)
        #print ("Reading from dmm %s = %s" % (self.name,data_str))
        #try:
        #    data_float = float(data_str)
        #except ValueError:
        #    print("\033[6;36HException %s on read_data(), ValueError = %s\n" % (self.name,data_str))
        #    return (0,float(0)) # Exception on float conversion, 0 = error
        #return (1,data_float) # Good read, 1 = converted to float w/o exception


    def read_data(self,cmd):
        data_float = 0.0
        data_str = ""
        self.inst.write(cmd)
        try:
            with Timeout(1):
                data_str = self.inst.read()
        except Timeout.Timeout:
            print ("Timeout exception from dmm %s on read_data() inst.read()\n" % self.name)
            return (0,float(0))
        #print ("Reading from dmm %s = %s" % (self.name,data_str))
        try:
            data_float = float(data_str)
        except ValueError:
            print("\033[6;36HException %s on read_data(), ValueError = %s\n" % (self.name,data_str))
            return (0,float(0)) # Exception on float conversion, 0 = error
        return (1,data_float) # Good read, 1 = converted to float w/o exception

    def get_data(self):
        self.status_flag,data = self.read_data("M?\r")
        if (self.status_flag):
            self.data = data#(data - 0.75) / 0.01 # Preamp A = 1000
        return self.data

    def get_data_status(self):
        return self.status_flag

    def vfd_msg(self, string):
        self.inst.write(":DISP:WIND:TEXT:DATA \"%s\";STAT ON;" % string)

print ("\033[2J")
print ("\033[10;10H")
dvm = vm_meter(6,1.0000,"VM02")

#for ci in range (65,91):
#    dvm.wrdat("%c0\n" % ci)
#    print ("%d %c0 written" % (ci, ci))
#    time.sleep(1)

strw = "G02"
dvm.wrdat("%s\n" % strw)
print ("%s written" % strw)
time.sleep(0.5)
dvm.wrdat("%s\n" % strw)
print ("%s written" % strw)
time.sleep(0.5)

for xi in range (0,3244):
    value = dvm.read_data("M?\n")
    time.sleep(0.10)
    errsr = dvm.read_data("E?\n")
    time.sleep(0.10)
    print ("\033[%d;60H Value = %s, Err %s" % (xi + 2, value[1], errsr) )
quit()