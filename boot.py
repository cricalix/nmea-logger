import webrepl
import gc
import network
from shipmodul import SSID, PASS
import utime

webrepl.start()
gc.collect()
do_connect()


def do_connect():
    '''
    Cribbed from the MicroPython docs. Sleep a bit on startup, then
    connect to the ShipModul wifi.

    TODO: Update the 2.4" TFT with network status for human feedback.
    '''
    utime.sleep(3)
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid=SSID, password=PASS)
        while not sta_if.isconnected():
            utime.sleep(2)
    print("Network config:", sta_if.ifconfig())
