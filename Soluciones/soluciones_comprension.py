# SOLUCIONES  EJERCICIOS   LIST COMPRENSIONES

# ejercicio 1

palabras = ['casa', 'perro', 'puerta', 'pizza']

palabra_titulo = [ palabra.title() for palabra in palabras ]

print (palabra_titulo)

# ejercicio 2

# listas = []
# tuplas = ()

personas = [ ('pedro',33), ('ana',3), ('juan',13), ('carla',45) ]

personas_mayores = [ per for per in personas if per[1] >= 18 ]

print (personas_mayores)
    
# ejercicio 3

multiplos_8 = [valor for valor in range (1,501) if valor % 8 == 0]

print (multiplos_8)

# ejercicio 4

numeros = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ] 

primos = [i for i in numeros if i % i == 0 if i % 2 != 0] 

print (primos)

# ejercicio 5

marcas_coches = [
    "Toyota", "Honda", "Ford", "Chevrolet", "BMW", "Mercedes-Benz",
    "Audi", "Volkswagen", "Nissan", "Tesla", "Hyundai", "Kia",
    "Subaru", "Porsche", "Ferrari"
]

marcas_cada_tres = [ marca for indice, marca in enumerate(marcas_coches) if indice % 3 == 0 ]

print (marcas_cada_tres)

