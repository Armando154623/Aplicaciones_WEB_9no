#Listas

# Ejercicio 1
# Imprimir una lista

# list = [5,8,7,6,5,8,2,4,6]
# for i in list:
#     print(i)

# Ejercicio 2
# Imprimir una lista de cadena

# list_2 = ["Juan", "Alberto", "Manolo", "Pedro", "Josh"]
# for i in list_2:
#     print(i)

# Ejercicio 3
# Imprimir una lista de cadena

# list_3 = [115, 12.05, "Pedro", "Juan", True, False]
# for i in list_3:
#     print(i)

# Recorrido diferente con la lista


# Agregar elementos a la lista

# lista = []
# lista.append(500)
# lista.append(300)
# for x in lista:
#     print(x)

# Pedir 10 numeros a la lista, ordenarlos e imprimirlos

lista = []
while(len(lista) < 10):
    lista.append(int(input("Ingresa un numero")))
lista.sort()
for x in lista:
    print(x)
