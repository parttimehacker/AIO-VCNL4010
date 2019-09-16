#!/usr/bin/python3
""" Shark Tank proof of concept for Nate """

# MIT License
#
# Copyright (c) 2019 Dave Wilson
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import time
import socket

# Simple example of sending and receiving values from Adafruit IO with the REST
# API client.
# Author: Tony DiCola
# Modified by Dave Wilson

# Import Adafruit IO REST client.
from Adafruit_IO import Client, RequestError, Feed

# Import the OLED display driver and the VCNL4010 sensor driver
import diyoled128x32
import diyvcnl4010

OLED = diyoled128x32.DiyOLED128x32()
OLED.show()

VCNL4010 = diyvcnl4010.DiyVCNL4010()
VCNL4010.calibrate()

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '1b95aaec576446d39c57fd7808a8ab39'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'NateWhiteSEA'

# Create an instance of the REST client.
AIO = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

TOPIC = socket.gethostname() + "light"

# Assign a light feed, if one exists already
try:
    LIGHT = AIO.feeds(TOPIC)
except RequestError: # Doesn't exist, create a new feed
    FEED = Feed(name=TOPIC)
    LIGHT = AIO.create_feed(FEED)

while True:
    time.sleep(30.0)
    VALUE = VCNL4010.get_ambient_value()
    INFO = "Measurement: " + "{0:.1f}".format(VALUE)
    OLED.set(1, INFO)
    TIME_STAMP = "Time Stamp:   " + time.strftime("%H:%M")
    OLED.set(2, TIME_STAMP)
    OLED.show()
    AIO.send_data(LIGHT.key, VALUE)
    time.sleep(30.0)
    OLED.clear()
