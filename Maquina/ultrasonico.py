#! /usr/bin/python
import RPi.GPIO as GPIO
import time 
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Trigger = 5
Echo = 27

GPIO.setup(Trigger, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)

print ("Sensor Ultrasonico")

try:
    while True:
        GPIO.output(Trigger,False)
        time.sleep(0.5)
        
        GPIO.output(Trigger, True)
        time.sleep(0.00001)
        GPIO.output(Trigger, False)
        inicio=time.time()
        
        while GPIO.input(Echo)==0:
            inicio=time.time()
            
        while GPIO.input(Echo)==1:
            final=time.time()
            
        t_transcurrido=final-inicio
        distancia=t_transcurrido*34000
        distacia=distancia/2
        
        print ("Distancia: " + str(distancia) + " cm")
        #print "Distancia= %.1fcm" %distancia
        if distancia >100 and distancia < 150:
            print ("Persona detectada")
            os.system("mpg123 -q Bienvenida1.mp3")
            time.sleep(5)
            
        elif distancia < 50:
            print("Bienvenido")
            time.sleep(2)
            os.system("mpg123 -q Bienvenida.mp3")
            os.system("/usr/bin/python Opciones.py")
            break
        
        elif distancia > 150:
            print("adios")
            time.sleep(2)
            os.system("mpg123 -q Adios.mp3")
            os.system ("/usr/bin/python ultrasonico.py")
        
#             if distancia < 50:1
#             print("Bienvenido")
#             time.sleep(2)
#             break
                            
except KeyboardInterrupt:
    GPIO.cleanup()
            