# Import required libraries
#!/usr/bin/python... 
import sys
import time
import RPi.GPIO as GPIO
import picamera
import datetime
from time import sleep
from subprocess import call

print " welcome to stepper motor and picamera code " 
camera = picamera.PiCamera()
# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use Physical pins 11,15,16,18 GPIO17,GPIO18,GPIO27,GPIO22
StepperPins = [17,18,27,22]

timelapseBetweenPics = 10

print " end 1"
# Set all pins as output
for pin in StepperPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
  
 
# Define advanced sequence
# as shown in manufacturers datasheet
Seq = [[1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1],
       [1,0,0,1]]

StepCount = len(Seq)-1
StepDir = 2 # Set to 1 or 2 for clockwise
            # Set to -1 or -2 for anti-clockwise

print " end 2" 			
# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)

# Initialise variables
StepCounter = 0

print " picamera end " 
#for x in range(1, 200):
 #   time.sleep(millisBetweenPics)
  #  nextpicname = '%d.jpg' % x
   # print "take pic %d" % x
    #camera.capture("/var/www/html/image/image" +nextpicname)
    # Start main loop while True:
for y in range (1, 5):
	nextpicname = '%d.jpg' % y
    #print "take pic %d" % y
    
	camera.capture("/var/www/html/image/image" +nextpicname)
	
	for x in range(0, 512):
		
		for halfstep in range(8):
		
			for pin in range(4): 
		
				GPIO.output(StepperPins[pin], Seq[halfstep][pin] )
			time.sleep(0.001)
	time.sleep(timelapseBetweenPics)	