"""Una matriz es simétrica si es igual a su transpuesta. Escribe un programa que verifique
si una matriz es simétrica."""

def es_simetrica(matriz):
    # Verificamos que la matriz sea cuadrada
    n = len(matriz)
    for fila in matriz:
        if len(fila) != n:
            return False

    # Verificamos si la matriz es simétrica
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True

def main():

    #Ingresar Matriz
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


    # Verificamos si la matriz es simétrica
    if es_simetrica(matriz):
        print("La matriz es SIMETRICA.")
    else:
        print("La matriz NO es simetrica.")


main()
