#! /bin/python3
import RPi.GPIO as GPIO
import os
import time
import mysql.connector
from mysql.connector import Error



try:
    conexion = mysql.connector.connect(
        host='localhost',
        user='admin',
        password='emb22',
        db='test2'
    )

    if conexion.is_connected():
        print("conexion exitosa")
        cursor = conexion.cursor()
        #nombre = input("Ingrese nombre de usuario: ")
        cursor.execute("UPDATE productos SET Cantidad = Cantidad - 1 WHERE Codigo = '4'")
        #sentencia = "INSERT INTO productos (Producto) VALUES (''{0}) ".format(Producto)
        #cursor.execute(sentencia)
        conexion.commit()
        print("registro ingresado con exito")
except Error as ex:
    print("error durante la conexion: ", ex)
finally:
    if conexion.is_connected():
        conexion.close()
        print("conexion finalizo")
        os.system ("/usr/bin/python monedas.py")
