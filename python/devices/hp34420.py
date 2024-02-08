# xDevs.com Python 10V test for 3458A
# http://xdevs.com/guide/ni_gpib_rpi/
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

class scpi_meter():
    temp = 38.5
    data = ""
    status_flag = 1
    temp_status_flag = 1

    def __init__(self,gpib,reflevel,name):
        self.gpib = gpib
        print ("\033[5;5H \033[0;31mGPIB[\033[1m%2d\033[0;31m] : HP 34420A\033[0;39m" % self.gpib)
        if cfg.get('teckit', 'interface') == 'gpib':
            self.inst = Gpib.Gpib(0, self.gpib, timeout = 180) # GPIB link
        elif cfg.get('teckit', 'interface') == 'vxi':
            self.inst = vxi11.Instrument(cfg.get('teckit', 'vxi_ip'), "gpib0,%d" % self.gpib) # VXI link
            self.inst.timeout = 180
        elif cfg.get('teckit', 'interface') == 'visa':
            self.inst = rm.open_resource('GPIB::%d::INSTR' % self.gpib)
            self.inst.timeout = 300000 # timeout delay in ms
        self.reflevel = reflevel
        self.name = name
        self.init_inst()

    def init_inst_dummy(self):
        # Setup SCPI DMM
        time.sleep(0.1)

    def init_inst(self):
        # Setup SCPI DMM
        #self.inst.clear()
        #self.inst.write("*RST")
        #self.inst.write("*CLR")
        self.inst.write(":CONF:VOLT:DC 0.0010, MAX, (@FRONt1)")
        self.inst.write(":SENS:FUNC 'VOLT:DC'")
        self.inst.write(":SENS:VOLT:DC:RES MAX")
        self.inst.write(":SENS:VOLT:DC:NPLC 50")
        #self.inst.write(":CONF:VOLT:DC 0.01, MAX, (@FRONt2)")
        #self.inst.write(":SENS:FUNC 'VOLT:DC'")
        #self.inst.write(":SENS:VOLT:DC:RES MAX")
        #self.inst.write(":SENS:VOLT:DC:NPLC 25")

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
        if (cmd >= 21e3):
            self.inst.write(":SENS:FRES:OCOM OFF")
        else:
            self.inst.write(":SENS:FRES:OCOM ON")
        self.inst.write(":SENS:FUNC 'FRES'")
        self.inst.write(":SENS:FRES:DIG 9;NPLC 20;AVER:COUN 10;TCON MOV")
        self.inst.write(":SENS:FRES:RANG %.2f" % cmd)

    def set_ohm_range(self,cmd):
        # Setup SCPI DMM
        self.inst.write(":SENS:FUNC 'RES'")
        self.inst.write(":SENS:RES:DIG 9;NPLC 10;AVER:COUN 10;TCON MOV")
        self.inst.write(":SENS:RES:OCOM OFF")
        self.inst.write(":SENS:RES:RANG %.2f" % cmd)

    def set_dcv_nrange(self,cmd,ch):
        # Setup SCPI DMM
        self.inst.write(":ROUT:TERM FRON%d" % ch)
        self.inst.write(":CONF:VOLT:DC %.4f, MAX, (@FRONt%d)" % (float(cmd),int(ch)))
        self.inst.write(":SENS:VOLT:DC:RES MAX")
        self.inst.write(":SENS:VOLT:DC:RANG %.4f" % float(cmd))
        self.inst.write(":SENS:VOLT:DC:NPLC 100")

    def read_data(self,cmd):
        data_float = 0.0
        data_str = ""
        self.inst.write(cmd)
        try:
            with Timeout(300):
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

    def get_adata(self):
        self.inst.write(":ROUT:TERM FRON1")
        self.status_flag,data = self.read_data("READ?")
        if (self.status_flag):
            self.data = data#(data - 0.75) / 0.01 # Preamp A = 1000
        return self.data

    def get_bdata(self):
        self.inst.write(":ROUT:TERM FRON2")
        self.status_flag,data = self.read_data("READ?")
        if (self.status_flag):
            self.data = data#(data - 0.75) / 0.01 # Preamp A = 1000
        return self.data

    def get_data(self):
        self.status_flag,data = self.read_data("READ?")
        if (self.status_flag):
            self.data = data#(data - 0.75) / 0.01 # Preamp A = 1000
        return self.data

    def get_data_status(self):
        return self.status_flag

