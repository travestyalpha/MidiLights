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
    #the for loop loops through the lights one at a time
    rndNumb1 = random.randint(4,7)
    rndNumb2 = random.randint(8,12)
    board.digital[rndNumb1].write(0)
    time.sleep(random.uniform(0.1,0.5))
    board.digital[rndNumb2].write(0)
    time.sleep(random.uniform(0.1,0.5))
    board.digital[rndNumb1].write(1)
    time.sleep(random.uniform(0.1,0.5))
    board.digital[rndNumb2].write(1)
    time.sleep(random.uniform(0.1,0.5))

    
        

