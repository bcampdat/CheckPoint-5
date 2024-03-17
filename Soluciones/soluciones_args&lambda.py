# SOLUCIONES  EJERCICIOS   ARGUMENTOS

####################################################################### ejercicio 1

def sumar(*args):
    print(args[0] + args[1] + args[2])

sumar(10, 7, 40)

####################################################################### ejercicio 2

def max_de_tres(num1, num2, num3):
    return max (num1, num2, num3)

# Ejemplo de uso de la función
num1 = 10
num2 = 5
num3 = 8

resultado = max_de_tres (num1, num2, num3)
print (resultado)
    
####################################################################### ejercicio 3

def nombre_completo (apellido="", nombre=""):
    print("Nombre completo:", nombre, apellido)

# Llamada a la función utilizando argumentos por nombre
nombre_completo(nombre="Juan", apellido="Pérez")
nombre_completo(apellido="Gómez", nombre="María")

####################################################################### ejercicio 4

def superposicion (lista1, lista2):
    for i in lista1:
        for x in lista2:
            if i == x:
                return True
    return False


####################################################################### ejercicio 5

def calificaciones (notas):
    notas_finales = []
    for nota in notas:
        if nota >= 7:
            notas_finales.append("Notable")
        elif nota >= 5:
            notas_finales.append("Aprobado")
        elif nota >= 2:
            notas_finales.append("Necesitas mejorar")
        else:
            notas_finales.append("Suspenso")
        
    return notas_finales

# Ejemplo de uso con 5 notas
notas = [8, 6, 9, 4, 7]
resultados = calificaciones(notas)
print("Calificaciones correspondientes:", resultados)

####### --------------------------------------------------------------------------------- ######    

# SOLUCIONES  EJERCICIOS   LAMBDA

####################################################################### ejercicio 1

cubo = lambda x: x ** 3
print(cubo(6))

####################################################################### ejercicio 2

convertir_mayusculas = lambda s: s.upper()
print(convertir_mayusculas("hola como estas?")) 

####################################################################### ejercicio 3

area_triangulo = lambda base, altura: (base * altura) / 2
print(area_triangulo(5, 8))

####################################################################### ejercicio 4

media = lambda x, y, z: (x + y + z) / 3
print(media(4, 5, 6))

####################################################################### ejercicio 5

media = lambda x, y, z: (x + y + z) / 3
print(media(4, 5, 6))