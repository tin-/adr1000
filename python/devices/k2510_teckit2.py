# -*- coding: utf-8 -*-
# $Id: devices/k2510.py | Rev 59  | 2022/07/05 20:58:16 tin_fpga $
# xDevs.com Keithley 2510 TEC SMU module
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
import ftplib
import numbers
import signal
import six
if six.PY2:
    import ConfigParser as ConfigParser
    cfg = ConfigParser.ConfigParser()
else:
    import configparser
    cfg = configparser.ConfigParser(inline_comment_prefixes=(';','#',))
    
    
cfg.read('teckit2.conf')
cfg.sections()
#from Adafruit_BME280 import *
#import k7168_client
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

val2 = 0.0
cnt = 0
tread = 20
rtd_temp = 0.0
tec_rtd = 0.3
tec_curr = 0.0
prev_t = 0
temp = 18
res_rtd = 0.3
tset = 18.0

#time.sleep(1)
#error,data = scan.send("*IDN?")
#print 'ID scanner... Error = ' + str(error) + ' : String = ' + str(data)
    
class Timeout():
  """Timeout class using ALARM signal"""
  class Timeout(Exception): pass

  def __init__(self, sec):
    self.sec = sec

  def __enter__(self):
    #signal.signal(signal.SIGALRM, self.raise_timeout)
    #signal.alarm(self.sec)
    print (" ")

  def __exit__(self, *args):
    #signal.alarm(0) # disable alarm
    print (" ")

  def raise_timeout(self, *args):
    raise Timeout.Timeout()

class tec_meter():
    temp = 38.5
    data = ""
    ppm = 0.0
    status_flag = 1
    temp_status_flag = 1
    global exttemp
    global rh
    global hectopascals
    global tec_rtd

    def __init__(self,gpib,reflevel,name):
        self.gpib = gpib
        print ("\033[4;5H \033[0;32mGPIB[\033[1m%2d\033[0;32m] : Keithley 2510\033[0;39m" % self.gpib)
        if cfg.get('teckit', 'interface') == 'gpib':
            self.inst = Gpib.Gpib(0, self.gpib, timeout = 180) # GPIB link
        elif cfg.get('teckit', 'interface') == 'vxi':
            self.inst = vxi11.Instrument(cfg.get('teckit', 'tec_ip'), "gpib0,%d" % self.gpib) # VXI link
            self.inst.timeout = 300
        elif cfg.get('teckit', 'interface') == 'visa':
            self.inst = rm.open_resource('GPIB::%d::INSTR' % self.gpib)
            self.inst.timeout = 300000 # timeout delay in ms

        self.reflevel = reflevel
        self.name = name
        self.tec_rtd = tec_rtd
        self.init_inst()
        
    def init_inst(self):
        # Setup SCPI DMM
        #self.inst.write("*rst") #reset TEC controller
        #self.inst.write("*CLR")
        #Set temperature transducer to thermistor and 4-wire sense mode
        self.inst.write(":sour:func:temp")
        self.inst.write(":sens:temp:tran rtd")      #select thermistor
        self.inst.write(":sens:temp:rtd:alph 0.00375") #10 kOhm thermistor
        self.inst.write(":sens:temp:rtd:beta 0.16") #10 kOhm thermistor
        self.inst.write(":sens:temp:rtd:delt 1.605") #10 kOhm thermistor
        self.inst.write(":sens:temp:rtd:rang 1000") #10 kOhm thermistor
        self.inst.write(":sens:temp:curr 8.333e-4") #10 kOhm thermistor
        self.inst.write(":syst:rsen on")            #4-wire mode enabled
        self.inst.write(":SYST:KEY 16")
        self.inst.write(":SYST:KEY 16")
        self.inst.write(":sour:temp:lcon:GAIN 330")            # P
        self.inst.write(":sour:temp:lcon:INT 0.05")          # I
        self.inst.write(":sour:temp:lcon:DER 0.2")            #D 

        #Set voltage limit
        self.inst.write(":sour:volt:prot 10.4") #+9.5V limit
        #Set current limit
        self.inst.write(":sens:curr:prot 4.05") #3.15A limit to allow 55C
        #Set temperature limit*
        self.inst.write(":sour:temp:prot:high 65")  #75C max temp
        self.inst.write(":sour:temp:prot:low 5")   #15C min temp
        self.inst.write(":sour:temp:prot:state ON") #enable temp #protection (default)

    def init_inst_ysi44006(self):
        # Setup SCPI DMM
        #self.inst.write("*rst") #reset TEC controller
        #self.inst.write("*CLR")
        self.inst.clear()
        #Set temperature transducer to thermistor and 4-wire sense mode
        self.inst.write(":sour:func:mode temp")
        self.inst.write(":sens:temp:tran THER")      #select thermistor
        self.inst.write(":SENS:TEMP:CURR 1e-4")
        self.inst.write(":sens:temp:THER:RANG 1e4") #10 kOhm thermistor
        self.inst.write(":sens:temp:THER:A 1.032e-3") #A
        self.inst.write(":sens:temp:THER:B 2.387e-4") #B
        self.inst.write(":sens:temp:THER:C 1.580e-7") #C
        self.inst.write(":syst:rsen off")            #4-wire mode disabled
        self.inst.write(":SYST:KEY 16")
        self.inst.write(":SYST:KEY 16")

        #Set voltage limit
        self.inst.write(":sour:volt:prot 10.5") #+9.5V limit
        #Set current limit
        self.inst.write(":sens:curr:prot 1.3") #2.5A limit
        #Set temperature limit
        self.inst.write(":sour:temp:prot:high 65")  #75C max temp
        self.inst.write(":sour:temp:prot:low 0")   #15C min temp
        self.inst.write(":sour:temp:prot:state ON") #enable temp #protection (default)

    def set_gain(self, gain):
        self.inst.write(":sour:temp:lcon:GAIN %6.4f" % gain)         # P

    def set_intg(self, intgr):
        self.inst.write(":sour:temp:lcon:INT %5.4f" % intgr)          # I

    def set_derv(self, derv):
        self.inst.write(":sour:temp:lcon:DER %5.4f" % derv)          # D

    def cfg_temp(self):
        self.inst.write(":sour:temp 20.0") #set temp
        self.inst.write(":OUTP ON")
        tec_rtd = 20.0

    def off_temp(self):
        self.inst.write(":OUTP OFF")

    def on_temp(self):
        self.inst.write(":OUTP ON")

    def set_tmp(self,tmp):
        string = float(tmp)
        global cnt
        #self.inst.write(":DISP:WIND2:TEXT:DATA \"SV %5.3f C, STEP %6d \";STAT ON;" % (tmp, cnt))
        #print ("Setting %2.1f" % string)
        self.inst.write(":sour:temp %2.3f" % (string + 0.20))
        time.sleep(0.001)

    def read_data(self,cmd):
        data_float = 0.0
        data_str = ""
        self.inst.write(cmd)
        try:
            with Timeout(20):
                data_str = self.inst.read()
        except Timeout.Timeout:
            print ("Timeout exception from dmm %s on read_data() inst.read()\n" % self.name)
            return (0,float(0))
        #print ("Reading from dmm %s = %s" % (self.name,data_str))
        try:
            data_float = float(data_str)
        except ValueError:
            print("\033[4;36H\033[31;1mException %s on read_data, ValueError = %s\n\033[39;1m" % (self.name,data_str))
            return (0,float(0)) # Exception on float conversion, 0 = error
        return (1,data_float) # Good read, 1 = converted to float w/o exception

    def get_data(self):
        global tec_rtd
        global tec_curr
        self.inst.clear()
        time.sleep(0.001)
        self.status_flag,data = self.read_data(":MEAS:CURR?")
        tec_curr = float(data)
        if (self.status_flag):
            self.data = data
        time.sleep(0.001)
        self.status_flag,data = self.read_data(":MEAS:TEMP?")
        if (self.status_flag):
            self.data = data
        tec_rtd = float(data)
        return tec_rtd,tec_curr

    def get_data_status(self):
        return self.status_flag

    def write_data(self,fileHandle):
        #print ("TEC TC:%2.3f " % (float(self.data) ) )
        tec_rtd = float(self.data)
        fileHandle.write(";%2.3f;\r\n" % tec_rtd);
        #print time.strftime("%d/%m/%Y-%H:%M:%S;") + ("\033[1;31m[%8d]: %2.8f , dev %4.2f ppm,\033[1;39m  EXT_T:%3.2f , RH:%3.2f , Press:%4.2f hPa" % (cnt, float(self.data),float(self.ppm),float(exttemp),float(rh),float(hectopascals) ) )
        #fileHandle.write (time.strftime("%d/%m/%Y-%H:%M:%S;") + ("%16.8f;%16.8f;%3.1f;%3.2f;%3.2f;%4.2f;\r\n" % (float(self.data),float(self.reflevel),float(self.ppm),float(exttemp),float(rh),float(hectopascals) ) ))

    def print_ppm(self):
        #self.inst.write(":DISP:WIND2:TEXT:DATA \"%3.3f ppm\"" % float(self.ppm))
        tec_rtd = float(self.data)
        #print ("%2.3f" % tec_rtd )
        #self.inst.write(":DISP:WIND2:TEXT:DATA \"  \"")
