"""Escribe un programa que permita al usuario ingresar una lista de números y filtre los
números primos.
Pista:
 Usa una función para verificar si un número es primo."""


def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def prueba():
    entrada = input("Ingrese una lista de números separados por espacios:")
    lista = list(map(int, entrada.split()))

    primos = [num for num in lista if es_primo(num)]

    if primos:
        print("Los números primos en la lista son:", primos)
    else:
        print("No hay números primos en la lista.")


prueba()
