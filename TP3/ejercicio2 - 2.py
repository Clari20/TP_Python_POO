"""Escribe un programa que calcule la suma de todos los elementos en una lista
bidimensional.
Pista: Aplique la función sum"""


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


suma_total = sum(sum(fila) for fila in matriz)



print("La matriz ingresada es:")
for fila in matriz:
    print(fila)

print(f"Y la suma de la matriz entera es: {suma_total}")
