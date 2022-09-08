"""
# Tema: Tuples
# Fecha: 31 de agosto del 2022
# Autor: Leonardo Martínez González
"""

"""
# 1. Definición. Es una colección de elementos inmutables.
# Las tuples son immutables y normalmente contienen una secuencia heterogénea
# de elementos que son accedidos al desempaquetar o indizar.

# 2. Crear tuples
tuple1 = tuple()
tuple2 = ()
tuple3 = (True, "Hola", 4, 15.16, "Final")

# 3. Accesar a elementos de la tuple, igual que en las listas
print(tuple3[1])

for x in tuple3:
    print(x)

# 4. Operaciones.
# 4.A. Son inmutables
# tuple3[1] = "5"

# 4.B. Las tuples pueden ser anidadas
grupoA = ("Jose luis", "Carmen", "Fabian")
grupoB = ("Luis", "Jose")
grupoC = (grupoA, grupoB)
print(grupoC)

numeros = ((3, 4), (4, 7), (7, 9))
print(numeros)

# 4.C. Las listas se pueden convertir en tuples haciendo uso de la función tuple()
lista1 = [5, 10, 15, 20, 25, 30]
tuple4 = tuple(lista1)
print(tuple4)

# 4.D. Se puede asignar el valor de una tuple con n elementos a n variables
alumno = (98456, "Jose Alberto Figueroa")
control, nombre = alumno
print("Alumno:", control, nombre)

# 5. Métodos de tuples
# count()
print(alumno.count(5))
# len()
print(len(alumno))
# index() Regresa el índice donde se ha encontrado, también puede pasarle un segundo
print(alumno.index(98456, 0, 1))

"""

'''
Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuples
con la siguiente forma:
(nombre, clave, destino)
Ejemplo:
pasajeros =    [("Felipe Gonzalez", 202101, "Guadalajara"),
                ("Guadalupe Salazar", 202110, "Zamora"),
                ("Ernesto Sotomayor", 202108, "Guadalajara"),
                ("Ruby Martinez", 202106, "León"),
                ("Jose Luis Bustamante", 202109, "Los Reyes"),
                ("Karina Tello", 202107, "Zamora"),
               ]

Además, en otra lista de tuples se almacenan los datos de cada ciudad y el estado al que pertenecen.
Ejemplo:
ciudades = [("Guadalajara","Jalisco"),
            ("Zamora","Michoacan"),
            ("León","Guanajuato"),
           ]

Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
- Agregar pasajeros a la lista de pasajeros
- Agregar ciudades a la lista de ciudades
- Dada la CLAVE de un pasajero, ver a que ciudad viaja
- Dada la CIUDAD, mostrar la cantidad de pasajeros que viajan a esa ciudad
- Dada la CLAVE de un pasajero, ver a que ESTADO viaja
- Dado un Estado, mostrar cuantos pasajeros viajan a ese Estado
- Salir del programa

NOTA: Haga uso de funciones
'''

pasajeros = [("Felipe Gonzalez", 202101, "Guadalajara"),
             ("Guadalupe Salazar", 202110, "Zamora"),
             ("Ernesto Sotomayor", 202108, "Guadalajara"),
             ("Ruby Martinez", 202106, "León"),
             ("Jose Luis Bustamante", 202109, "Los Reyes"),
             ("Karina Tello", 202107, "Zamora")]
ciudades = [("Guadalajara", "Jalisco"),
            ("Zamora", "Michoacan"),
            ("León", "Guanajuato")]

while True:
    print("\n")
    print("1) Agregar pasajeros", "2) Agregar ciudad", "3) Ver a que ciudad viaja un pasajero")
    print("4) Mostrar la cantidad de pasajeros que viajan a una ciudad", "5) Ver a que ESTADO viaja un pasajero")
    print("6) Mostrar cuantos pasajeros viajan a un Estado", "7) Salir del programa")
    print("\n")

    opcion = int(input("Selecciona una opcion"))
    if opcion == 1:
        pasajeros.append((input("Dame el nombre"), int(input("Ingrese un codigo")), input("Dame la ciudad")))

    elif opcion == 2:
        ciudades.append((input("Dame la ciudad"), input("Dame el estado")))

    elif opcion == 3:
        codigo = int(input("Dame el codigo del pasajero"))
        ciudad = ""
        for x in range(0, len(pasajeros)):
            if pasajeros[x][1] == codigo:
                ciudad = pasajeros[x][2] + ""
        if ciudad != "":
            print("El pasajero viaja a la ciudad de", ciudad)
        else:
            print("El pasajero no existe")

    elif opcion == 4:
        ciudad = input("Dame la ciudad")
        cantidad = 0
        for x in range(0, len(pasajeros)):
            if pasajeros[x][2] == ciudad:
                cantidad += 1
        print("Son", cantidad, "pasajero(s) los que viajan a", ciudad)

    elif opcion == 5:
        codigo = int(input("Dame el codigo del pasajero"))
        estado = ""
        for x in range(0, len(pasajeros)):
            if pasajeros[x][1] == codigo:
                ciudad = pasajeros[x][2]
                for y in range(0, len(ciudades)):
                    if ciudades[y][0] == ciudad:
                        estado = ciudades[y][1]
                        break
        if estado != "":
            print("El pasajero viaja al estado de", estado)
        else:
            print("No se encontro")

    elif opcion == 6:
        estado = input("Dame el estado")
        cantidad = 0
        for x in range(0, len(ciudades)):
            if ciudades[x][1] == estado:
                ciudad = ciudades[x][0]
                for y in range(0, len(pasajeros)):
                    if pasajeros[y][2] == ciudad:
                        cantidad += 1
                break

        print("Son", cantidad, "pasajero(s) los que viajan a", estado)
    elif opcion == 7:
        break
    else:
        print("Opcion incorrecta")

print("Vuelva pronto")
