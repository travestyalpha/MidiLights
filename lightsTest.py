# This script will cycle through four pin on the Arduino using pyFirmata
# The pins are designated by the variable n
# They will stay on for t time, and off for t time.
# Once all the pins are cycled through, the script ends.

# -*- coding: utf-8 -*-
import time
from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0') #designate the correct com port to use
board.digital[4].write(1) #R1
board.digital[5].write(1) #R2
board.digital[6].write(1) #R3
board.digital[7].write(1) #R4
board.digital[8].write(1) #R5
board.digital[9].write(1) #R6
board.digital[10].write(1) #R7
board.digital[11].write(1) #R8
time.sleep(1)
#choice = int(input("which light strand do you want to turn on? : "))
#n = choice
#t  = float(input("How long do you want it to turn on for? (in seconds) : "))
t = .1
board.digital[4].write(0)
time.sleep(t)
board.digital[4].write(1)
time.sleep(t)
board.digital[5].write(0)
time.sleep(t)
board.digital[5].write(1)
time.sleep(t)
board.digital[6].write(0)
time.sleep(t)
board.digital[6].write(1)
time.sleep(t)
board.digital[7].write(0)
time.sleep(t)
board.digital[7].write(1)
time.sleep(t)
board.digital[8].write(0)
time.sleep(t)
board.digital[8].write(1)
time.sleep(t)
board.digital[9].write(0)
time.sleep(t)
board.digital[9].write(1)
time.sleep(t)
board.digital[10].write(0)
time.sleep(t)
board.digital[10].write(1)
time.sleep(t)
board.digital[11].write(0)
time.sleep(t)
board.digital[11].write(1)
time.sleep(t)

print "Test Completed"
