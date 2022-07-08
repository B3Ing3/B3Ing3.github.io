#! /bin/python3
import RPi.GPIO as GPIO
import os
import time
#from tqdm import tqdm   para barra de carga

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)    #Dulces a elegir 1
GPIO.setup(20, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)

print("Que opcion deseas elegir? :) ")
while True:
    inputValue = GPIO.input(21)                          #Elegir Chocolate
    if(inputValue == True):
        print("Seleccionaste Chocolate :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateChocolate.py")
        
    inputValue2 = GPIO.input(20)                           #Elegir Bombones
    if(inputValue2 == True):
        print("Seleccionaste Bombones :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateBombones.py")      
        
    inputValue3 = GPIO.input(13)                           #Elegir Escuincles
    if(inputValue3 == True):
        print("Seleccionaste Escuincles :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateEscuincles.py")
        
    inputValue4 = GPIO.input(19)                           #Elegir Sabritas
    if(inputValue4 == True):
        print("Seleccionaste Sabritas :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateSabritas.py")
        
    inputValue5 = GPIO.input(26)                           #Elegir Mazapan
    if(inputValue5 == True):
        print("Seleccionaste Mazapan :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateMazapan.py")