#!/usr/bin/env python

# MIT License
#
# Copyright (c) 2017 Adrien Lecharpentier
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

from blinkt import set_pixel, set_brightness, show, clear
import time, colorsys, sys, getopt

spacing = 360.0 / 16.0
hue = 0
brightness = 0.04
duration = 5.0

def show_usage():
  print 'rainbow.py -d <duration> -b <brightness>'

def should_it_continue(start_time, duration):
  now = time.time()
  return (now - start_time) < duration

def rainbow(duration, brightness):
  set_brightness(brightness)
  start = time.time()
  while should_it_continue(start, duration):
    hue = int(time.time() * 100) % 360
    for x in range(8):
      offset = x * spacing
      h = ((hue + offset) % 360) / 360.0
      r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
      set_pixel(x, r, g, b)
    show()
    time.sleep(0.01)

def main(argv):
  try:
    opts, args = getopt.getopt(argv, "d:b:", ["duration=", "brightness="])
  except getopt.GetoptError:
    show_usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      show_usage()
      sys.exit()
    elif opt in ("-d", "--duration"):
      duration = float(arg)
    elif opt in ("-b", "--brightness"):
      brightness = float(arg)
  rainbow(duration, brightness)

if __name__ == "__main__":
  main(sys.argv[1:])
