#! /bin/python3
import RPi.GPIO as GPIO
from gtts import gTTS
import os
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)    #Opcion 1
GPIO.setup(23, GPIO.IN)    #Opcion 2
GPIO.setup(18, GPIO.IN)    #Opcion 3
#GPIO.setup(21, GPIO.IN)    #Comida elegir 1
##Rreproduccion de audio de 3 opciones.
os.system("mpg123 -q Opciones2.mp3")
time.sleep(1.0)

while True:
    inputValue = GPIO.input(24)  #OPCION DE COMIDA
    #inputValue2 = GPIO.input(21)
    if(inputValue == True):
    	print("Seleccionaste la opcion 1:\n1_Galletas Oreo:14$\n2_Hot-dog:21$\n3_Mantecadas:15$\n4_Barritas de fresa:17$\n5_Conchas Bimbo:27$")
    	os.system("mpg123 -q Comida2.mp3")
    	os.system ("/usr/bin/python Comida.py")
    	time.sleep(.3)
    time.sleep(.01)
        #os.system ("/usr/bin/python Comida.py")
    
    
    inputValue = GPIO.input(23)  #OPCION DE BEBIDAS
    #inputValue2 = GPIO.input(21)
    if(inputValue == True):        
    	print("Seleccionaste la opcion 2:\n1_Coca-cola:15$\n2_Fanta 700ml:14$\n3_Manzanita de lata:15$\n4_Pepsi de lata:17$\n5_Agua Ciel 900ml:17$")
    	os.system("mpg123 -q Bebidas2.mp3")
    	os.system ("/usr/bin/python bebidas.py")
    	time.sleep(.3)
    time.sleep(.01)
    
    inputValue = GPIO.input(18)  #OPCION DE DUlCES
    #inputValue2 = GPIO.input(21)
    if(inputValue == True):
    	print("Seleccionaste la opcion 3:\n1_Chocolate:10$\n2_Bombones:17$\n3_Escuincles:8$\n4_Sabritas:14$\n5_Mazapan:5$")
    	os.system("mpg123 -q Dulces2.mp3")
    	os.system ("/usr/bin/python dulces.py")
    	time.sleep(.3)
    time.sleep(.01)
    


