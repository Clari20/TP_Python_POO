"""Escribe un programa que calcule la transpuesta de una matriz. La transpuesta de una
matriz intercambia sus filas por columnas."""

filas = int(input("Ingrese la cantidad de filas: "))
col = int(input("Ingrese la cantidad de columnas: "))


matriz = []


for i in range(filas):
    entrada = input(f"Ingrese los valores de la fila {i + 1} separados por espacios: ")
    fila = list(map(int, entrada.split()))
    if len(fila) != col:
        print(f"Error: La fila {i + 1} debe tener {col} elementos.")
        exit()
    matriz.append(fila)



print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

transpuesta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print(transpuesta)