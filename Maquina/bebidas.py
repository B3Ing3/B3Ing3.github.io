#! /bin/python3
import RPi.GPIO as GPIO
import os
import time
#from tqdm import tqdm   para barra de carga

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)    #Elegir Bebidas
GPIO.setup(20, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)

print("Que opcion deseas elegir? :) ")
while True:
    inputValue = GPIO.input(21)                          #Elegir Coca
    if(inputValue == True):
        print("Seleccionaste Coca-Cola :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateCoca.py")
        
    inputValue2 = GPIO.input(20)                           #Elegir Fanta
    if(inputValue2 == True):
        print("Seleccionaste Fanta :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateFanta.py")      
        
    inputValue3 = GPIO.input(13)                           #Elegir Manzanita
    if(inputValue3 == True):
        print("Seleccionaste Manzanita :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateManzanita.py")
        
    inputValue4 = GPIO.input(19)                           #Elegir Pepsi
    if(inputValue4 == True):
        print("Seleccionaste Pepsi :)")
        time.sleep(1)
        os.system ("/usr/bin/python updatePepsi.py")
        
    inputValue5 = GPIO.input(26)                           #Elegir Agua
    if(inputValue5 == True):
        print("Seleccionaste Agua Natural :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateAgua.py")