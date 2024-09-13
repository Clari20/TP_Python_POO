"""Crea una función que reciba dos parámetros: el número de filas y columnas. La función
debe generar una matriz de ese tamaño, donde los valores son números enteros
consecutivos empezando desde 1."""

filas = int(input("Ingrese la cantidad de filas: "))
col = int(input("Ingrese la cantidad de columnas: "))

i = 1

matriz = []


for fila in range(filas):
    fila_actual = []
    for elemento in range(col):
        fila_actual.append(i)
        i += 1
    matriz.append(fila_actual)

for fila in matriz:
    print(fila)


