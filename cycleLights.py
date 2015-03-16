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

print("The lights are now running\n")

while True:
    #the for loop loops through the lights one at a time
    for x in range(0,8):
        pin = x
        t = .5
        board.digital[x + 4].write(0)
        time.sleep(t)
        board.digital[x + 4].write(1)
        print("Pin %d " % (x + 4) + "\n")

    
        

