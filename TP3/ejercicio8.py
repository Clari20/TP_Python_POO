"""Escribe un programa que identifique y muestre los elementos que se repiten en una
lista.

Pista:
Utiliza un diccionario o un conjunto (set) para hacer el seguimiento de los
elementos."""

def encontrar_repetidos(lista):
    vistos = set()
    repetidos = set()

    for elemento in lista:
        if elemento in vistos:
            repetidos.add(elemento)
        else:
            vistos.add(elemento)

    return repetidos

def prueba():
    
    entrada = input("Ingrese una lista de elementos separados por espacios: ")
    lista = entrada.split()

    repetidos = encontrar_repetidos(lista)

    if repetidos:
        print("Los elementos que se repiten son:", repetidos)
    else:
        print("No hay elementos repetidos.")

prueba()
