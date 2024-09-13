"""Escribe un programa que permita al usuario ingresar una lista de números y calcule el
promedio de los elementos."""


entrada = input("Ingrese una lista de números separados por espacios: ")


num = list(map(int, entrada.split()))
long = len(num)
suma = sum(num)

div = int(suma/long)

print(f"El promedio de {num} es: {div}")