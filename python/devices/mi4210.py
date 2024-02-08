# -*- coding: utf-8 -*-
# $Id: devices/mi4210.py | Rev 65  | 2022/09/07 00:17:23 tin_fpga $
# xDevs.com MI 6010B module
# Copyright (c) 2012-2019, xDevs.com
# 
# Python 3 | RPi3 
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

err_cnt = 0
    
cfg.read('teckit.conf')
cfg.sections()

if cfg.get('teckit', 'interface') == 'gpib':
    import Gpib
elif cfg.get('teckit', 'interface') == 'vxi':
    import vxi11
elif cfg.get('teckit', 'interface', 1) == 'visa':
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

class dcc_scan():
    temp = 38.5
    data = ""
    status_flag = 1
    temp_status_flag = 1

    def __init__(self,gpib,reflevel,name):
        self.gpib = gpib
        print ("\033[9;5H \033[0;33mGPIB[\033[1m%2d\033[0;35m] : MIL 4210A\033[0;39m" % self.gpib)
        if cfg.get('teckit', 'interface') == 'gpib':
            self.inst = Gpib.Gpib(0, self.gpib, timeout = 180) # GPIB link
        elif cfg.get('teckit', 'interface') == 'vxi':
            self.inst = vxi11.Instrument(cfg.get('teckit', 'vxi_ip'), "gpib0,%d" % self.gpib) # VXI link
        elif cfg.get('teckit', 'interface', 1) == 'visa':
            self.inst = rm.open_resource('GPIB::%d::INSTR' % self.gpib)
            self.inst.timeout = 300000 # timeout delay in ms
        #self.inst = vxi11.Instrument("192.168.1.2", "gpib0,15") # VXI link
            self.inst.timeout = 160
        self.reflevel = reflevel
        self.name = name
        self.init_inst()

    def init_inst_dummy(self):
        # Setup SCPI DMM
        time.sleep(0.1)

    def init_inst(self):
        # Setup SCPI DMM
        self.inst.clear()
        self.inst.write("00A\r")
        self.inst.write("00B\r")
        print ("\033[s\033[5;105H Init completed, S sent\033[u")

    def read_rstb(self):
        data_stb = self.inst.read_stb()
        print ("\033[s\033[11;105HSTB "),
        print (data_stb)
        time.sleep(1)

    def wait_ready(self):
        datas = self.inst.read_stb()
        while (datas == 0):
            datas = self.inst.read_stb()
            time.sleep(0.5)

    def sel_cha(self,cha):
        self.inst.write("%02dA\r" % int(cha))
        print ("\033[s\033[1;155H A-CH = %02d\033[u" % int(cha))

    def sel_chb(self,chb):
        self.inst.write("%02dB\r" % int(chb))
        print ("\033[s\033[2;155H B-CH = %02d\033[u" % int(chb))
