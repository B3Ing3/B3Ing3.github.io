#! /bin/python3
import RPi.GPIO as GPIO
import os
import time
import mysql.connector
from mysql.connector import Error
#from tqdm import tqdm   para barra de carga

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)    #Comida elegir 1
GPIO.setup(20, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)

print("Que opcion deseas elegir? :) ")
while True:
    inputValue = GPIO.input(21)                          #Elegir Galletas Oreo
    if(inputValue == True):
        print("Seleccionaste Galletas oreo :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateGalletas.py")
        
    inputValue2 = GPIO.input(20)                           #Elegir Hot-dog
    if(inputValue2 == True):
        print("Seleccionaste Hot-Dog :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateHot.py")      
        
    inputValue3 = GPIO.input(13)                           #Elegir Mantecada
    if(inputValue3 == True):
        print("Seleccionaste Mantecadas :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateMantecada.py")
        
    inputValue4 = GPIO.input(19)                           #Elegir Barritas
    if(inputValue4 == True):
        print("Seleccionaste Barritas :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateBarritas.py")
        
    inputValue5 = GPIO.input(26)                           #Elegir Conchas
    if(inputValue5 == True):
        print("Seleccionaste Conchas Bimbo :)")
        time.sleep(1)
        os.system ("/usr/bin/python updateConchas.py")