"""Escribe un programa que permita al usuario ingresar una lista y un número, y cuente
cuántas veces aparece ese número en la lista."""

entrada = input("Ingrese una lista de números separados por espacios:")

lista = list(map(int, entrada.split()))

num = int(input("Ingrese el indice del valor que desea encontrar: "))


apariciones = lista.count(num)

print(f"El valor {num} se encuentra {apariciones} veces")