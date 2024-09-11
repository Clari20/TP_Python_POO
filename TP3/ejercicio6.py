"""Escribe un programa que permita al usuario ingresar una lista de números y elimine los
elementos duplicados.
Pista:
Utiliza la función set()."""


entrada = input("Ingrese una lista de números separados por espacios: ")


num = list(map(int, entrada.split()))


numeros_sin = list(set(num))


print(f"Lista sin duplicados: {numeros_sin}")
