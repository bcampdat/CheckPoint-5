# SOLUCIONES  EJERCICIOS   CONDICIONALES

####################################################################### ejercicio 1

a = 50
b = 10

# Si a es mayor a b…
if a > b:
    print("Hola Mundo")

####################################################################### ejercicio 2

age = int(input("¿Cuál es tu edad? "))

if age < 18: 
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
    
#@####################################################################### ejercicio 3

n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")

######################################################################### ejercicio 4

puntos = 120

precio_final_de_compra = 100  # Precio inicial antes de aplicar el descuento

if puntos < 100:
    precio_final_de_compra *= 0.9  # 10% de descuento
    
elif puntos < 150:
    precio_final_de_compra *= 0.88  # 12% de descuento
    
elif puntos < 150:
    precio_final_de_compra *= 0.85  # 15% de descuento
    
else:
    precio_final_de_compra *= 0.8  # 20% de descuento
    

print(f"El precio final de compra con {puntos} puntos es: {precio_final_de_compra} €")

######################################################################## ejercicio 5

# Pedir al usuario que ingrese dos valores, a y b
a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))

# Pedir al usuario que ingrese la operación deseada
operacion = int(input("Selecciona la operación a realizar (1: suma, 2: multiplicación, 3: resta, 4: división): "))

# Realizar la operación seleccionada
if operacion == 1:
    resultado = a + b
elif operacion == 2:
    resultado = a * b
elif operacion == 3:
    resultado = a - b
elif operacion == 4:
    if b != 0:
        resultado = a / b
    else:
        resultado = "No es posible dividir por cero"
else:
    resultado = "Operación no válida"

# Mostrar el resultado de la operación
print(f"El resultado de la operación seleccionada es: {resultado}")

####### --------------------------------------------------------------------------------- ######    

# SOLUCIONES EJERCICIOS   BUCLES

####################################################################### ejercicio 1

for i in range(1, 11):
    print(i)

####################################################################### ejercicio 2

#      *     
#     ***    
#    *****   
#   *******  
#  *********
# ***********

z = 7
x = 1
while z > 0:
    print(' ' * z + '*' * x + ' ' * z)
    x+=2
    z-=1

######################################################################## ejercicio 3

import time

contador = 10

while contador >= 0:
    print(contador)
    time.sleep(1)  # Espera 1 segundo
    contador -= 1

print("Fuego!!")

######################################################################## ejercico 4

PIN_SECRETO = "1234"
intentos_maximos = 3

for intento in range(1, intentos_maximos + 1):
    pin = input("Introduce el PIN: ")
    
    if pin == PIN_SECRETO:
        print("¡Login correcto!")
        break
    else:
        if intento < intentos_maximos:
            print("PIN incorrecto. Intenta de nuevo.")
        else:
            print("¡Llamando a la policía!")

##################################################################### ejercico 5 
   
#           **************************       Reto ✔        **************************


palabra = "Python".upper()
longitud_palabra = len(palabra)
letras_acertadas = ['_'] * longitud_palabra
intentos_maximos = 6
intentos_realizados = 0

while True:
    print(" ".join(letras_acertadas))

    if '_' not in letras_acertadas:
        print("¡Felicidades! Has adivinado la palabra.")
        break

    letra = input("Ingresa una letra: ").upper()

    if letra in letras_acertadas:
        print("Ya has ingresado esa letra. Intenta de nuevo.")
        continue

    if letra in palabra:
        for i in range(longitud_palabra):
            if palabra[i] == letra:
                letras_acertadas[i] = letra
    else:
        intentos_realizados += 1
        print(f"Letra incorrecta. Llevas {intentos_realizados} intentos fallidos.")

        if intentos_realizados == intentos_maximos:
            print("Fin del juego. ¡Te has quedado sin intentos!")
            print(f"La palabra era: {palabra}")
            break


##########################################        Enhorabuena!!!    👌    eres un crack  👍