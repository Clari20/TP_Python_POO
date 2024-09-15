"""Escribe un programa que extraiga los elementos de la diagonal principal de una matriz
cuadrada."""

def extraer_diagonal_principal(matriz):
    # Verificamos que la matriz sea cuadrada
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            raise ValueError("La matriz no es cuadrada")

    # Extraemos los elementos de la diagonal principal
    diagonal = [matriz[i][i] for i in range(n)]
    return diagonal

def main():
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

    # Extraemos la diagonal principal
    diagonal = extraer_diagonal_principal(matriz)

    # Imprimimos la diagonal principal
    print("Diagonal principal:", diagonal)


main()
