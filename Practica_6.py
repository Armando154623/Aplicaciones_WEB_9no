'''
Tema: conjuntos
Fecha: 05 de septiembre del 2022
Autor: Leonardo Martínez González
'''


"""
# 1. Definición. en Python es utilizado para trabajar con conjuntos de elementos.
#    La principal característica de este tipo de datos es que es una colección cuyos elementos
#    no guardan ningún orden y que además son únicos.
#    los principales usos de esta clase se usan para conocer si un elemento pertenece o no
#    a una colección y eliminar duplicados de un tipo secuencial (list, tuple o str).

# 2. Creación. Para crear un conjunto, basta con encerrar una serie de elementos entre llaves {},
#    o bien usar el constructor de la clase set() y pasarle como argumento un objeto iterable
#    (como una lista, una tupla, una cadena …).

lista1 = [5, "Fernando", True]

conjunto0 = set(i for i in range(0, 10, 2))
conjunto1 = {"Pedro", False, 8, "Juan", 3.1416}
conjunto2 = set(lista1)

print(conjunto0)
print(conjunto1)
print(conjunto2)

#    Usando la función forezenset. es inmutable y su contenido no puede ser modificado
#    una vez que ha sido inicializado

caracteres = []
for i in range(65, 91):
    caracteres.append(chr(i))

print(caracteres)

conjunto4 = frozenset(caracteres)

print(conjunto4)

#    Los elementos repetidos se eliminan


# 3. Para acceder a los elementos de un conjunto. Dado que los conjuntos son colecciones
#    desordenadas, en ellos no se guarda la posición en la que son insertados los elementos
#    como ocurre en los tipos list o tuple. Es por ello que no se puede acceder a los elementos
#    a través de un índice.

print(conjunto1["Fernando"])

# 4. Añadir elementos: con el método add() ó con el método update()
#    Agregar el numero 8 al conjunto c

conjunto2.add(8)
print(conjunto2)

#    Agregar varios elementos al conjunto

conjunto2.update({29, 36, 48})
conjunto1.update({True, False, True})

print(conjunto2)
print(conjunto1)

# 5. Eliminar elementos del conjunto: discard(elemento), remove(elemento), pop() y clear()
#    discard(elemento) y remove(elemento) son muy parecidos, solo que remove lanza una excepcion KeyError
#    en caso de no existir el elemento


conjunto2.discard(29)
print(conjunto2)


#     pop() devuelve un elemento aleatorio y lo elimina, si el conjunto esta vacio lanza una
#     excepcion KeyError.

print(conjunto2.pop())

#    El método clear() elimina todos los elementos del conjunto

conjunto2.clear()

#    Número de elementos en un conlunto con la función len()

print(len(conjunto1))

#    Verificar si un elemento esta dentro de un conjunto



# ************************ Operaciones con conjuntos
# 1. Union  ( | )

conjunto1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
conjunto2 = {6, 7, 8, 9, 10}
conjunto3 = {30, 31, 32, 33}
conjunto4 = {33, 32, 31, 30}

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)

resultado1 = conjunto1 | conjunto2


print("Resultado con |:", resultado1)

# 2. Intersección ( & )

resultado2 = conjunto1 & conjunto2
print("Resultado con &:", resultado2)


# 3. Diferencia ( - )

resultado3 = conjunto1 - conjunto2
print("Resultado con -:", resultado3)


# 4. Diferencia simétrica ( ^ ). es el conjunto que contiene los elementos de A y B
#    que no son comunes.

resultado4 = conjunto1 ^ conjunto2
print("Resultado con ^:", resultado4)


# 5. Inclusión de conjuntos.  Se utiliza el operador <= para comprobar si un conjunto A
#    es subconjunto de B y el operador >= para comprobar si un conjunto A es superconjunto de B.

resultado5 = conjunto2 <= conjunto1
resultado6 = conjunto1 <= conjunto2
print("Resultado con B y A (<= >=):",  resultado5)
print("Resultado con A y B (<= >=):",  resultado6)

# 5. Conjuntos disjuntos. Dos conjuntos A y B son disjuntos si no tienen elementos en común,
#    es decir, la intersección de A y B es el conjunto vacío.

resultado7 = conjunto3 <= conjunto2
print("Resultado con B y C (<= >=):",  resultado7)

# 6. Igualdad de conjuntos. En Python dos conjuntos son iguales si y solo si todos los elementos
#    de un conjunto están contenidos en el otro. Esto quiere decir que cada uno es un subconjunto
#    del otro.

resultado8 = conjunto4 == conjunto3
print("Resultado con D y C (==):",  resultado8)

"""

'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes.
2. Crear un método que regrese un conjunto de tuplas de materias.
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"",
                "Promedio":
            },
            {
                "Nombre":"",
                "Promedio":
            },
            . . . 
        ],
        "Promedio general": 
   }


'''
import json

archEstu = open("Archivos/Estudiantes.prn", mode="r")
archKardex = open("Archivos/Kardex.txt", mode="r")
mJson = open("Archivos/Alumno.json", mode="w")

if archEstu.readable() and archKardex.readable():
    estudiantes = []
    kardex = []
    # Obtenemos los alumnos
    for est in archEstu.read().split("\n"):
        if len(est) > 0:
            estudiantes.append((est[0:8], est[8:]))
    print(estudiantes)

    # Obtenemos las materias
    for kar in archKardex.read().split("\n"):
        if len(kar) > 0:
            datos = kar.split("|")
            kardex.append((datos[0], datos[1], datos[2]))
    print(kardex)

    # Obtenemos el numero de control por el usuario
    noControl = input("Dame un numero de control")

    informacion = {}
    materias = []
    promedio = 0
    for i in range(0, len(estudiantes)):
        if estudiantes[i][0] == noControl:
            for j in range(0, len(kardex)):
                if kardex[j][0] == noControl:
                    materias.append({"Nombre": kardex[j][1], "Promedio": kardex[j][2]})
                    promedio += int(kardex[j][2])
            informacion = {"Nombre": estudiantes[i][1], "Materias": materias, "Promedio General": (promedio / len(materias))}

    json.dump(informacion, mJson)
else:
    print("No se puede leer un archivo")

archEstu.close()
archKardex.close()
mJson.close()




