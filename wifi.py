import network
import shipmodul


def connect():
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
        sta_if.connect(ssid=shipmodul.SSID, password=shipmodul.PASS)
        while not sta_if.isconnected():
            utime.sleep(2)
    print("Network config:", sta_if.ifconfig())