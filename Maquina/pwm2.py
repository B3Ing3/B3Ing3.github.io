#! /usr/bin/python

import RPi.GPIO as GPIO
import time
import sys

angle2=int(sys.argv[1])

servoPin=18
pwmFreq=50

def degToDuty(angle2):
	return int((angle2-0)*(10-1)/(180-0)+1)



GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPin , GPIO.OUT)
servo=GPIO.PWM(servoPin,pwmFreq)
servo.start(0)
servo.ChangeDutyCycle(degToDuty(angle2)) #25 100 200
time.sleep(1)
servo.stop()
GPIO.cleanup()
        