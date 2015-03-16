# -*- coding: utf-8 -*-
import time
import random
from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0') #designate the correct com port to use

for x in range (4, 12):
    board.digital[x].write(1)
time.sleep(.5)

print("The lights are now running\n")

while True:
    #the lights ramp up all turning on, the pause, flash a few time, than
    #all ramp off. pause a few seconds, then repeat

    for x in range(4,12):
        board.digital[x].write(0)
        time.sleep(0.1)
    time.sleep(1)
    for x in range(0,4):
        rndNum = random.randint(4,12)
        board.digital[rndNum].write(1)
        time.sleep(random.uniform(0.2,1))
        board.digital[rndNum].write(0)
        time.sleep(random.uniform(0.2,1))
    time.sleep(1)
    for x in range(4,12):
        board.digital[x].write(1)
        time.sleep(0.1)
    time.sleep(1)
    for x in range(0,4):
        rndNum = random.randint(4,12)
        board.digital[rndNum].write(0)
        time.sleep(random.uniform(0.2,1))
        board.digital[rndNum].write(1)
        time.sleep(random.uniform(0.2,1))
    time.sleep(1)

    
        

