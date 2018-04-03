import gc
import network
import utime
import webrepl
import wifi
from shipmodul import PASS, SSID

webrepl.start()
gc.collect()
wifi.connect()
