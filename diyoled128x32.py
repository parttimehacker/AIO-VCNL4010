#!/usr/bin/python3
""" Manage OLED 128x32 display light """

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

import socket

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# pylint: disable=bad-whitespace
# pylint: disable=too-many-public-methods

import Adafruit_SSD1306

class DiyOLED128x32:
    """ OLED display 128 by 32 """

    def __init__(self,):
        """ Initialize the VCNL40xx sensor """
        self.disp = Adafruit_SSD1306.SSD1306_128_32(rst=24)
        self.disp.begin()
        self.disp.clear()
        # Create image buffer. Make sure to create image with mode '1' for 1-bit color.
        self.image = Image.new('1', (self.disp.width, self.disp.height))
        self.font = ImageFont.truetype("../fonts/Tahoma.ttf",10)
        # Some nice fonts to try: http://www.dafont.com/bitmap.php
        self.draw = ImageDraw.Draw( self.image )
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #connect to any target website
        sock.connect(('portseattle.org', 0))
        host_name = socket.gethostname()
        ip_address = sock.getsockname()[0]
        sock.close()
        self.line = [host_name + ": " + ip_address, "Measurement:", "Time Stamp: "]

    def reset(self,):
        """ reset the device to the default condition """
        self.disp.clear()
        self.disp.display()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #connect to any target website
        sock.connect(('portseattle.org', 0))
        host_name = socket.gethostname()
        ip_address = sock.getsockname()[0]
        sock.close()
        self.line = [host_name + ": " + ip_address, "Measurement:", "Time Stamp: "]

    def set(self, line=2, val=""):
        """ set the specified line with text which will be displayed on show() """
        if line == 1:
            self.line[1] = val
        elif line ==2:
            self.line[2] = val

    def show(self,):
        """ clear and display 3 lines of text """
        self.disp.clear()
        self.draw.rectangle((0,0,self.disp.width,self.disp.height), outline=0, fill=0)
        self.draw.text((0,0),  self.line[0], font=self.font, fill=255)
        self.draw.text((0,11), self.line[1], font=self.font, fill=255)
        self.draw.text((0,22), self.line[2], font=self.font, fill=255)
        self.disp.image(self.image)
        self.disp.display()

    def clear(self,):
        """ clear display """
        self.disp.clear()
        self.disp.display()

if __name__ == '__main__':
    exit()
