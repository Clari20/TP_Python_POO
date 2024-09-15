"""Escribe un programa que gire una lista bidimensional (matriz) 90 grados en el sentido
de las agujas del reloj."""

def girar_matriz_90(matriz):
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    matriz_girada = [[0] * num_filas for _ in range(num_columnas)]

    # Giramos la matriz 90 grados en el sentido de las agujas del reloj
    for i in range(num_filas):
        for j in range(num_columnas):
            matriz_girada[j][num_filas - 1 - i] = matriz[i][j]

    return matriz_girada

def main():
    # Ejemplo de matriz
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Giramos la matriz 90 grados en el sentido de las agujas del reloj
    matriz_girada = girar_matriz_90(matriz)


    print("Matriz original:")
    for fila in matriz:
        print(fila)

    
    print("\nMatriz girada 90 grados en el sentido de las agujas del reloj:")
    for fila in matriz_girada:
        print(fila)


main()
