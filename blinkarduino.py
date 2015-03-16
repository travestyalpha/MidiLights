# -*- coding: utf-8 -*-
import time
from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0')
n = 1
while True:
     print n
     board.digital[12].write(1)
     time.sleep(.5)
     board.digital[12].write(0)
     time.sleep(.5)
     n += 1
     if n == 5:
          break
print "Completed"
