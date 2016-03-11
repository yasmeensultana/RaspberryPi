# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import picamera
import datetime
from time import sleep
from subprocess import call

camera = picamera.PiCamera()
# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signals to use Physical pins 11,15,16,18 GPIO17,GPIO22,GPIO23,GPIO24
StepPins = [17,18,27,22]

millisBetweenPics =10

# Set all pins as output
for pin in StepPins:
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

# Read wait time from command line
if len(sys.argv)>1:
  WaitTime = int(sys.argv[1])/float(1000)
else:
  WaitTime = 10/float(1000)
print WaitTime
# Initialise variables
StepCounter = 0

for x in range(1, 200):
    time.sleep(millisBetweenPics)
    nextpicname = '%d.jpg' % x
    print "take pic %d" % x
    camera.capture("/home/pi/workspace/picamera/image"+nextpicname)
    # Start main loop while True:
    for x in range(0, 2000):
      for pin in range(0, 4):
        xpin = StepPins[pin]
        #print StepCounter
        #print pin
        if Seq[StepCounter][pin]!=0:
    #      print " Step %i Enable %i" %(StepCounter,xpin)
          GPIO.output(xpin, True)
        else:
          GPIO.output(xpin, False)
      StepCounter += StepDir

      # If we reach the end of the sequence start again
      if (StepCounter>=StepCount):
        StepCounter = 0
      if (StepCounter<0):
        StepCounter = StepCount

      # Wait before moving on
      time.sleep(0.001)
