[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# NMEA Logger

This NMEA Logger is designed to run on chips supported by MicroPython. It was born out of a need for a NMEA logging system for a boat, where the data would be automatically grouped by day.

# Hardware

This code is targeted at an ESP8266 board, but anything supported by MicroPython will probably work. YMMV.

# Installation

* Get yourself an ESP8266 board
* Flash it to MicroPython using esptool
* Push the .mpy versions of the .py files in this project to the board
* Reset your board