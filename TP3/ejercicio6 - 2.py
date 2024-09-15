"""Escribe un programa que multiplique cada elemento de una lista bidimensional por un
valor escalar dado por el usuario."""

def multiplicar_matriz_por_escalar(matriz, escalar):
    return [[elemento * escalar for elemento in fila] for fila in matriz]

def main():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    escalar = float(input("Ingrese el valor escalar: "))

    matriz_resultante = multiplicar_matriz_por_escalar(matriz, escalar)

    print("Matriz resultante:")
    for fila in matriz_resultante:
        print(fila)


main()
