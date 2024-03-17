# SOLUCIONES  EJERCICIOS   MODULOS (PiP)

# ejercicio 1
import math


resultado = math.sqrt(16)

print(resultado)  

# ejercicio 2

import numpy as np



num = np.array([1, 2, 3, 4, 5])

 
media = np.mean(num)

print(media) 
    
# ejercicio 3

import datetime


now = datetime.datetime.now()

print(now)

# ejercicio 4

import pandas as pd


# Leer un archivo de Excel
df = pd.read_excel('archivo.xlsx')

# ejercicio 5

import random

 
dado1=random.randint(1,6)
dado2=random.randint(1,6)
suma =dado1+dado2
 
print("El primer dado vale: ",dado1)
print("El segundo dado vale: ",dado2)
print("La suma de los dados es: ",suma)
 
if suma==9:
    print("Has ganado")
else:
    print("Has perdido")
