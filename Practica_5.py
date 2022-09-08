'''
Tema: Diccionarios, archivos y formato JSON
Fecha: 02 de septiembre del 2022
Autor: Leonardo Martínez González


# 1. Definición. Colección no ordenada de objetos. Está formada por un PAR clave: valor.
#    Las claves pueden ser números, cadenas o cualquier otro tipo inmutable.
#    Los valores pueden ser de cualquier tipo, incluso otros diccionarios.

d2 = {"d1": {"Homero": "Fox", "Kilos": "Gramos"}, "d3": {"Monopoli": "Turista", "Kansas": 18}, "Juan": "Martinez"}

# 2. Crear diccionarios

estudiantes = {"Juan": 15, "Pedro": 8, "Ramirez": 10, "Benito": 7}

# 3. Acceder a sus valores. Se accede igual que las listas pero por su clave en lugar del indice
#    Si no existe la clave se lanza la excepcion KeyError

# 4. Recorrer un diccionario por su clave.

# 5. Recorrer un diccionario por su valor

# 6. Recorrer un diccionario por clave: valor

for clave, valor in estudiantes.items():
    print("Clave:", clave, "Valor", valor)

# 7. Agregar elementos a un diccionario
print(estudiantes)
estudiantes[2] = "Guadalupe"
print(estudiantes)

# 8. Eliminar elementos con del

del estudiantes[2]
print(estudiantes)

# 9. Modificar, accesando directo a la posición

estudiantes[8] = "Gunter"
print(estudiantes)

# 10. Algunas operaciones comunes
#     Contar elementos

print("Estudiantes", len(estudiantes))

#     Saber si existe un elemento dentro de un diccionario (solo por clave)

print(4000 in d2)

#     Para vaciar un diccionario

d2.clear()
print(d2)

#     Unir o actualizar dos diccionarios

d1 = {"Uno": 1, "Dos": 2, "Tres": 3}
d2 = {"Cuatro": 4, "Cinco": 5, "Seis": 6}

d1.update(d2)
print(d1)
print(d2)

#     Sacar un elemento del diccionario con pop() muy parecido a get(), pero pop(),
#     regresa el elemento y lo elimina del diccionario

valor = d1.pop("Uno")
print("Valor:", valor, "Lista: ", d1)

#      Tambien acepta devolver un valor por defecto pop(clave, "valor por defecto)

valor = d1.pop("Ocho", 8)
print("Valor:", valor, "Lista: ", d1)

#      popitem() regresa un elemento (par clave:valor) de forma aleatoria y lo remueve
#      si no existe genera una excepción KeyError

print(d2.popitem())
print(d2.popitem())


#      generar un diccionario a partir de una lista con el metodo fromkeys() con valores
#      por defecto con valor None o 0 (CERO)

lista1 = []
d3 = {}
for x in range(2,101,2):
    lista1.append(x)
d3 = dict.fromkeys(lista1, 0)
print(lista1)
print(d3)


Defina un diccionario Estudiantes, que:
Almacene datos personales y todas las materia que ha cursado con sus promedios.
Las actividades complemetarias que ha tomado.


estudiantes = \
{
    17854360:
    {
        "Nombre": "Juan Alcazar Martinez",
        "Sexo": "H",
        "Altura": 1.78,
        "Edad": 19,
        "Materias":
        {
            40404: {"Nombre": "Matematicas", "Promedio": 98.8},
            80465: {"Nombre": "Filosofia", "Promedio": 75},
            74156: {"Nombre": "Biologia", "Promedio": 90},
            98542: {"Nombre": "Historia", "Promedio": 85},
            98452: {"Nombre": "Calculo", "Promedio": 90}
        }
    },

    19856745:
    {
        "Nombre": "Alonso Barragan Valencia",
        "Sexo": "H",
        "Altura": 1.70,
        "Edad": 19,
        "Materias":
        {
            40404: {"Nombre": "Matematicas", "Promedio": 90},
            80465: {"Nombre": "Filosofia", "Promedio": 80},
            74156: {"Nombre": "Biologia", "Promedio": 70},
            98542: {"Nombre": "Historia", "Promedio": 70},
            98452: {"Nombre": "Calculo", "Promedio": 75}
        }
    },

    18450365:
    {
        "Nombre": "Alfredo Calderon Figueroa",
        "Sexo": "H",
        "Altura": 1.75,
        "Edad": 19,
        "Materias":
        {
            40404: {"Nombre": "Matematicas", "Promedio": 80},
            80465: {"Nombre": "Filosofia", "Promedio": 80},
            74156: {"Nombre": "Biologia", "Promedio": 95},
            98542: {"Nombre": "Historia", "Promedio": 80},
            98452: {"Nombre": "Calculo", "Promedio": 70}
        }
    },

    18540498:
    {
        "Nombre": "Carlos Martinez Medina",
        "Sexo": "H",
        "Altura": 1.72,
        "Edad": 19,
        "Materias":
        {
            40404: {"Nombre": "Matematicas", "Promedio": 62},
            80465: {"Nombre": "Filosofia", "Promedio": 70},
            74156: {"Nombre": "Biologia", "Promedio": 75},
            98542: {"Nombre": "Historia", "Promedio": 80},
            98452: {"Nombre": "Calculo", "Promedio": 70}
        }
    },

    20154687:
    {
        "Nombre": "Juan Valencia Maldonado",
        "Sexo": "H",
        "Altura": 1.60,
        "Edad": 19,
        "Materias":
        {
            40404: {"Nombre": "Matematicas", "Promedio": 90},
            80465: {"Nombre": "Filosofia", "Promedio": 75},
            74156: {"Nombre": "Biologia", "Promedio": 69},
            98542: {"Nombre": "Historia", "Promedio": 80},
            98452: {"Nombre": "Calculo", "Promedio": 100}
        }
    },
}

for est in estudiantes.items():
    print(est)


El directorio de los clientes de una empresa está organizado en una cadena de texto como la de
más abajo, donde cada línea contiene la información: nombre, email, teléfono, nss, y el descuento
que se le aplica. Las líneas se separan con el carácter de cambio de línea \n 
y la primera línea contiene los nombres de los campos con la información contenida en el directorio.

"NSS;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

Escribir un programa que genere un diccionario con la información del directorio, 
donde cada elemento corresponda a un cliente y tenga por clave su NSS y por valor otro diccionario
con el resto de la información del cliente. Los diccionarios con la información de cada cliente
tendrán como claves los nombres de los campos y como valores la información de cada cliente
correspondientes a los campos. Es decir, un diccionario como el siguiente:

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
{'01234567L': {'Nombre': 'Luis González', 'Email': 'luisgonzalez@mail.com', 'Telefono': '656343576', 'Descuento': 12.5}, '71476342J': {'Nombre': 'Macarena Ramírez', 'Email': 'macarena@mail.com', 'Telefono': '692839321', 'Descuento': 8.0}, '63823376M': {'Nombre': 'Juan José Martínez', 'Email': 'juanjo@mail.com', 'Telefono': '664888233', 'Descuento': 5.2}, '98376547F': {'Nombre': 'Carmen Sánchez', 'Email': 'carmen@mail.com', 'Telefono': '667677855', 'Descuento': 15.7}}
considere el método de cadena split() que separa una cadena de acuerdo al caracter que se le pase


cadena = "NSS;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

diccionario = {}
lista = cadena.split("\n")
definicion = lista[0].split(";")

for x in range(1, len(lista)):
    cliente = {}
    datos = lista[x].split(";")
    for j in range(0, len(definicion)):
        cliente[definicion[j]] = datos[j]
    diccionario[x] = cliente

print(diccionario)


Ejercicio: Crear un diccionario con los códigos postales y su localidad del estado de San Luis Potosi,
           para ello descargue la tabla de códigos postales de la siguiente dirección: 
           https://www.correosdemexico.gob.mx/SSLServicios/ConsultaCP/CodigoPostal_Exportar.aspx
           
           el formato del diccionario  tendra la forma:
           {109159: {'CP': '78000', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, 
            109160: {'CP': '78037', 'Municipio': 'San Luis Potosí', 'Estado': 'San Luis Potosí'}, . . . }
           
           Genere una lista con los VALORES del diccionario anterior.
           Guarde en un archivo con formato JSON los resultados
           
           Consideraciones:
           1. El método split regresa un arreglo al separar una cadena en subcadenas.
           2. El municipio se encuentra en la posición 4.
           3. El estado se llama: "San Luis Potosí"
'''
import json

codigosPostales = {}
municipios = []

archivo = open("Archivos/San Luis Potosí.txt", mode="r")
mJson = open("Archivos/San Luis Potosí.json", mode="w")

if archivo.readable():
    municipios = archivo.read().split("\n")
    indice = 0
    for mun in municipios[2:]:
        municipio = {}
        indice += 1
        datos = mun.split("|")
        if len(datos) > 4:
            municipio["CP"] = datos[0]
            municipio["Municipio"] = datos[3]
            municipio["Estado"] = datos[4]
            codigosPostales[indice] = municipio
    json.dump(codigosPostales, mJson)
else:
    print("No se pudo abrir el archivo")

mJson.close()
archivo.close()

'''
Formto  JSON
Formato ligero de intercambio de datos
medio de comunicación estadarizado entre lenguajes de programación

en Python se leen facilmente archivos JSON 
import json #libreria que maneja este formato
with open("Nombre_archivo", 'w') as archivo:
        json.dump( Lista_de_diccionario, archivo) # dump es disparar

Las lineas anteriores graban un archivo y su contenido es en formato JSON

'''