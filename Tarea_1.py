
"""
'r' - Abierto para lectura (por defecto)
'w' - Abierto para escritura, truncando primero el fichero
'x' - Abierto para creación en exclusiva, falla si el fichero ya existe
’a’ - Abierto para escritura, añadiendo al final del fichero si este existe
'b' - modo binario
’t’ - modo texto (por defecto)
’+’ - abierto para actualizar (lectura y escritura)
"""

# Abrimos un archivo de texto
archivo = open("Archivos/Lista_de_nombres.txt", mode="r")
if archivo.readable():
    print(archivo.read())
else:
    print("Imposible leer el archivo")
archivo.close()