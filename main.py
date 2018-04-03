from machine import Timer
import machine
import rgb
import ili9431


if __name__ == "__main__":
    '''
    MicroPython will call this code on startup, after boot.py has run. This 
    makes boot.py a good place to initialise the network stack, leaving this 
    code to do the heavy lifting.

    Use timers and callbacks to listen for data, then go idle() for a period 
    of time. Works whether the board has just booted, or has been running for 
    a while.

    Timestamps need to be pulled from GPS data coming in via NMEA sentences, 
    because the ESP8266 has a terrible RTC. Adafruit offer hardware for their
    Feather line of boards that implements a battery-backed RTC. However,
    given this code is meant to be logging NMEA data on a boat, which will 
    invariably involve a GPS source, the time can be pulled from there.
    '''
    pass
