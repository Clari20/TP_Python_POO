"""Crea un programa que genere una matriz identidad de tamaño n. Una matriz identidad
es una matriz cuadrada donde los elementos de la diagonal principal son 1 y el resto
son 0."""


def generar_matriz_identidad(n):
    # Crear una matriz n x n llena de ceros
    matriz = [[0 for _ in range(n)] for _ in range(n)]

    # Establecer los elementos de la diagonal principal a 1
    for i in range(n):
        matriz[i][i] = 1

    return matriz

def main():
    
    n = int(input("Ingrese el tamaño de la matriz identidad: "))

    matriz_identidad = generar_matriz_identidad(n)

    print("Matriz identidad de tamaño", n, ":")
    for fila in matriz_identidad:
        print(fila)


main()
