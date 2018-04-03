from micropython import const

"""
ShipModul 3Wi edition uses a defined SSID and password. These will
need to be changed appropriately before installing boot.py on the
microcontroller.

http://www.shipmodul.com/downloads/manuals/MiniPlex-3_EN.pdf
"""

SSID = const("MiniPlex")
PASS = const("MiniPlex")
IP = const("10.0.0.1")
PORT = const("10110")
