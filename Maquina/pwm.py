#! /usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
servo1 = GPIO.PWM(4,50) 
servo1.start(0)
#GPIO.setwarnings(False)
duty = 10

while True:
    duty <= 18
    servo1.ChangeDutyCycle(duty)
    time.sleep(1)
    duty = duty + 1
    time.sleep(0.5)

#print ("Volviendo a 0 grados")
    servo1.ChangeDutyCycle(2)
    time.sleep(0.5)
    servo1.ChangeDutyCycle(0)
    servo1.stop()
GPIO.cleanup()