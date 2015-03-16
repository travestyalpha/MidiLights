# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox
import time
from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0') #designate the correct com port to use

top = Tkinter.Tk()

def light1():
    board.digital(4).write(0)
    time.sleep(1)
    board.digital(4).write(1)

def light2():
    board.digital(5).write(0)
    time.sleep(1)
    board.digital(5).write(1)

def light3():
    board.digital(6).write(0)
    time.sleep(1)
    board.digital(6).write(1)

def light4():
    board.digital(7).write(0)
    time.sleep(1)
    board.digital(7).write(1)

def light5():
    board.digital(8).write(0)
    time.sleep(1)
    board.digital(8).write(1)

def light6():
    board.digital(9).write(0)
    time.sleep(1)
    board.digital(9).write(1)

def light7():
    board.digital(10).write(0)
    time.sleep(1)
    board.digital(10).write(1)

def light8():
    board.digital(11).write(0)
    time.sleep(1)
    board.digital(11).write(1)

B1 = Tkinter.Button(top, text = "Light1", command = light1)

B2 = Tkinter.Button(top, text = "Light2", command = light2)

B3 = Tkinter.Button(top, text = "Light3", command = light3)

B4 = Tkinter.Button(top, text = "Light4", command = light4)

B5 = Tkinter.Button(top, text = "Light5", command = light5)

B6 = Tkinter.Button(top, text = "Light6", command = light6)

B7 = Tkinter.Button(top, text = "Light7", command = light7)

B8 = Tkinter.Button(top, text = "Light8", command = light8)
        

