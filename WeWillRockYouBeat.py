# -*- coding: utf-8 -*-
import time, sched
from datetime import timedelta
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
time.sleep(5)

print("The lights are now running\n")

while True:
    # We Will Rock You beat
    
    #first beat
    board.digital[4].write(0)
    board.digital[6].write(0)
    board.digital[7].write(0)
    time.sleep(.3)
    board.digital[4].write(1)
    board.digital[6].write(1)
    board.digital[7].write(1)
    time.sleep(.1)
    
    #second beat
    board.digital[4].write(0)
    board.digital[6].write(0)
    board.digital[7].write(0)
    time.sleep(.3)
    board.digital[4].write(1)
    board.digital[6].write(1)
    board.digital[7].write(1)
    time.sleep(.1)
    
    #3rd beat
    board.digital[5].write(0)
    board.digital[8].write(0)
    board.digital[9].write(0)
    board.digital[10].write(0)
    time.sleep(.4)
    board.digital[5].write(1)
    board.digital[8].write(1)
    board.digital[9].write(1)
    board.digital[10].write(1)
    time.sleep(.1)

    time.sleep(.3)
    
        
