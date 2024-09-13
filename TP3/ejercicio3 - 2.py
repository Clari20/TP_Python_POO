"""Modifica el programa anterior para que imprima la suma de cada fila de la lista
bidimensional."""


filas = int(input("Ingrese la cantidad de filas: "))
col = int(input("Ingrese la cantidad de columnas: "))

matriz = []

# Pedir al usuario que ingrese los valores de cada fila
for i in range(filas):
    entrada = input(f"Ingrese los valores de la fila {i + 1} separados por espacios: ")
    fila = list(map(int, entrada.split()))
    if len(fila) != col:
        print(f"Error: La fila {i + 1} debe tener {col} elementos.")
        exit()
    matriz.append(fila)

# Calcular la suma de cada fila
sumas_filas = [sum(fila) for fila in matriz]

# Imprime la matriz
print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

# Imprime la suma de cada fila
print("La suma de cada fila es:")
for i, suma in enumerate(sumas_filas):
    print(f"Fila {i + 1}: {suma}")
