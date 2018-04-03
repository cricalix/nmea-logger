[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

# NMEA Logger

This NMEA Logger is designed to run on chips supported by MicroPython. It was born out of a need for a NMEA logging system for a boat, where the data would be automatically grouped by day.

# Hardware

This code is targeted at an ESP8266 board, but anything supported by MicroPython will probably work. YMMV.

# Installation

In general, this is what you'll be doing:

* Get yourself an ESP8266 board
* Flash it to MicroPython using esptool
* Download the MicroPython tarball that matches the binary you flashed to your board
* Build the mypy-cross tool, and the Unix port of MicroPython
* Use the Unix port to run upip and install some libraries from PyPi
* Pull some other libraries via git clone
* Use the cross-compiler to convert the various library .py files to .mpy files
* Push the library .mpy files across to flash (via ampy, for instance) in /lib/whatever
* Use the cross-compiler to convert the .py files of this project to .mpy files (except boot.py, main.py)
* Push the .mpy across to flash, in /
* Reset your board

## Firmware

From a standard Python 3 (or 2 if you insist, but really, use 3) installation, install ampy and esptool. On Linux, you may need to prefix this with 'sudo'.

    pip install ampy
    pip install esptool

Download the [MicroPython firmware](http://micropython.org/download) for your board, and flash it to the board using esptool.

**Windows**

    esptool.py.exe --port com3 --baud 406800 write_flash --flash_size=detect -fm dio 0x00000 esp8266-DATE-VER.bin

The port will depend on your particular installation of Windows (in that it may have other COM ports allocated), and may rely on the Arduino IDE being installed directly from arduino.cc to get the virtual port driver. The Microsoft Store edition did not appear to ship with any USB serial port drivers.

## MicroPython cross-compile

The easiest way I've found to deal with this is use the Adafruit Vagrant setup for cross-compiling, blowing away everything they've installed, and doing a fresh git clone for the needed bits. Assuming you've got some kind of *nix environment (instructions tested in a Vagrant/VirtualBox Ubuntu 16.04 install):

Build the ESP Open SDK:

    git clone https://github.com/pfalcon/esp-open-sdk.git
    cd esp-open-sdk
    make STANDALONE=y

* Modify ~/.profile to put **esp-open-sdk/xtensa-lx106-elf/bin** at the head of the PATH
* Download MicroPython's [source code](https://github.com/micropython/micropython/releases), matching the version to the pre-built firmware build version

Build the cross-compiler and MicroPython Unix port:
    
    cd micropython-x.y.z
    make -C mpy-cross
    cd ports/unix
    make axtls
    make

## Libraries

To deal with the fact that ESP8266 boards have a small amount of RAM, it helps to cross-compile the library .py files to bytecode .mpy files.

### pynmea2
Install pynmea2, and cross-compile it to .mpy

    cd ~
    micropython-x.y.z/ports/unix/micropython -m upip install pynmea2
    ... output about ~/.micropython/lib
    for f in $(find .micropython/lib/pynmea2 -name '*.py'); do \
        micropython-x.y.z/mpy-cross/mpy-cross $f ; done

Use a tool like ampy to copy the lib/pynmea2 structure to the board's flash, but only the .mpy files, not the .py files

### Adafruit RGB
This only applies if you're using the 2.4" TFT display.

    cd ~
    git clone https://github.com/adafruit/micropython-adafruit-rgb-display.git
    cd micropython-adafruit-rgb-display
    for f in rgb.py ili9431.py ; do \
        micropython-x.y.z/mpy-cross/mpy-cross $f ; done

Use a tool like ampy to copy those two .mpy files to the root of the board's flash.


# Programming notes

* https://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html
* https://docs.micropython.org/en/latest/esp8266/esp8266/general.html