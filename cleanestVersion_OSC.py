from OSC import OSCServer,OSCClient, OSCMessage
import sys
from time import sleep
import time
import types
import os
import RPi.GPIO as GPIO

server = OSCServer( ("192.168.1.42", 8080) )#This has to be the IP of the RaspberryPi on the network
client = OSCClient()

def handle_timeout(self):
	print ("I'm IDLE")
#This here is just to do something while the script recieves no information....
server.handle_timeout = types.MethodType(handle_timeout, server)

# FADERS
#################################################################################################################################################
def fader(path, tags, args, source): 
	value=int(args[0])#Value is the variable that will transform the input from the faders into whole numbers(easier to deal with); it will also get the 'y' value of the XP pads
	print "Fader Value:", value
	


# XY PADS
###############################################################################################################################################
def xypad(path, tags, args, source):
	 yy=int(args[0])
	 xx=int(args[1])#Value 2 is used with XP pads, it will get the 'x' value
	 print "Value of Y:", yy,  "    Value of X:", xx
	 

 
# BUTTONS
####################################################################################################################################################
def kill_switch(path, tags, args, source):
	state=int(args[0])
	print "Kill Switch:", state
	if state == 1:
		server.close()#THIS IS THE EMERGENCY KILL BUTTON!

def autopilot(path, tags, args, source):
	state=int(args[0])
	print "Autopilot: ", state;
      


# ACCELEROMETER (will onyl work if you have the Accelerometer option on, in the TouchOSC app)
###################################################################################################################################################
def accel(path, tags, args, source):
	y=float(args[0])
	x=float(args[1])
	z=float(args[2])
	print "X:", x
	print "Y:", y 
	print "Z:", z
	print " "
	time.sleep(3);


#These are all the add-ons that you can name in the TouchOSC layout designer (you can set the values and directories)
server.addMsgHandler("/1/fader1",fader)
server.addMsgHandler("/1/xy1", xypad)
server.addMsgHandler("/1/toggle1", kill_switch)
server.addMsgHandler("/1/toggle2", autopilot)
server.addMsgHandler("accxyz", accel)#The Accelerometeer Values
#The way that the MSG Handlers work is by taking the values from set accessory, then it puts them into a function
#The function then takes the values and separates them according to their class (args, source, path, and tags)

while True:
	server.handle_request()

server.close()
#This will kill the server when the program ends
