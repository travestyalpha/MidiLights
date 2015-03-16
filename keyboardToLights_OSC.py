from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import time
import types
import os
import RPi.GPIO as GPIO
import binascii

from pyfirmata import Arduino, util
board = Arduino('/dev/ttyACM0')

server = OSCServer( ("192.168.1.42", 8080) )#This has to be the IP of the RaspberryPi on the network
client = OSCClient()

def handle_timeout(self):
	print ("I'm IDLE")
        #This here is just to do something while the script recieves no information....


def button1(a,b,c,d):
    print "message received %s" % OSC.getUrlStr(source)
    print "with addr: %s" % addr
    print "typetages %s" % tags
    print "data %s" % stuff
    board.digital[4].write(0)
    time.sleep(1)
    board.digital[4].write(1)

def button2(a,b,c,d):
    print "message received"
    board.digital[5].write(0)
    time.sleep(1)
    board.digital[5].write(1)

def button3(a,b,c,d):
    print "message received"
    board.digital[6].write(0)
    time.sleep(1)
    board.digital[6].write(1)

def button4(a,b,c,d):
    print "message received"
    board.digital[7].write(0)
    time.sleep(1)
    board.digital[7].write(1)

def button5(a,b,c,d):
    print "message received"
    board.digital[8].write(0)
    time.sleep(1)
    board.digital[8].write(1)

def button6(a,b,c,d):
    print "message received"
    board.digital[9].write(0)
    time.sleep(1)
    board.digital[9].write(1)

def button7(a,b,c,d):
    print "message received"
    board.digital[10].write(0)
    time.sleep(1)
    board.digital[10].write(1)


def button8(a,b,c,d):
    print "message received"
    board.digital[11].write(0)
    time.sleep(1)
    board.digital[11].write(1)


server.addMsgHandler("/1/C", button1)
server.addMsgHandler("/1/D", button2)
server.addMsgHandler("/1/E", button3)
server.addMsgHandler("/1/F", button4)
server.addMsgHandler("/1/G", button5)
server.addMsgHandler("/1/A", button6)
server.addMsgHandler("/1/B", button7)
server.addMsgHandler("/1/CC", button8)

#The way that the MSG Handlers work is by taking the values from set accessory, then it puts them into a function
#The function then takes the values and separates them according to their class (args, source, path, and tags)

while True:
	server.handle_request()

server.close()
#This will kill the server when the program ends
