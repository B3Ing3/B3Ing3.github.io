#!/usr/bin/python
from gtts import gTTS
import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(21, GPIO.IN)

count = 0
count2 = 0
count3 = 0
#count4 = 0
cambiomac=100
cambiocliente=0
G=14
H=21
B=17
C=27

C2=15
F2=14
M2=15
P2=17
A2=15





print ("\\\\\\\\\\POR FAVOR INGRESA EL DINERO//////////")
print ("Cuando finalice presione A")
try:
    while True:
    	suma=count
    	suma2=count2*5
    	suma3=count3*10
    	#suma4=count4*50
    	total=suma+suma2+suma3#+suma4
        cambiocliente=cambiomac-total
       
        
        if cambiocliente < 0:
            os.system("mpg123 -q cambio.mp3")
            break
        

    	inputValue = GPIO.input(24)
    	if(inputValue == True):
    		count = count + 1
    		print("Insertado " + str(count) + " monedas de 1$." "..........Acumulado: " + str(total+1) + "|||||CAMBIO DISPONIBLE: " + str(cambiocliente-1))
    		time.sleep(.3)
    	time.sleep(.01)

    	inputValue2 = GPIO.input(23)
    	if(inputValue2 == True):
    		count2 = count2 + 1
    		print("Insertado ")+ str(count2) + " monedas de 5$. " "..........Acumulado: " + str(total+5) + "|||||CAMBIO DISPONIBLE: "+str(cambiocliente-5)
    		time.sleep(.3)
    	time.sleep(.01)
  
        inputValue3 = GPIO.input(18)
     	if(inputValue3 == True):
    		count3 = count3 + 1
    		print("Insertado ")+ str(count3) + " monedas de 10$. " "...........Acumulado: " + str(total+10) +  "|||||CAMBIO DISPONIBLE: "+str(cambiocliente-10)
     		time.sleep(.3)
     	time.sleep(.01)

#         inputValue4 = GPIO.input(6)
#     	if(inputValue4 == True):
#     		count4 = count4 + 1
#     		print("Insertado ")+ str(count4) + " billete de 50$." "...........Acumulado: " + str(total+50) + "|||||CAMBIO DISPONIBLE: "+str (cambiocliente-50)
#     		time.sleep(.3)
#     	time.sleep(.01)
    	
    	
    	inputValue5 = GPIO.input(21)
    	if(inputValue5 == True):
            print("...\nEntregando su pedido")
            os.system("mpg123 -q entrega.mp3")
            #os.system("/usr/bin/python variable.py")
            os.system ("/usr/bin/python pwm.py")
            
####################################################################

    #while True:
#         if cambiomac == 0:
#             os.system("mpg123 -q hola3.mp3")
#             break
    	
finally:
	GPIO.cleanup()