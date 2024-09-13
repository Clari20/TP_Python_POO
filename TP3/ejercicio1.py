"""Escribe un programa que permita al usuario ingresar una lista de números y calcule la
suma de todos los elementos en la lista."""


lista = []

while True:
    elemento = int(input("Ingrese un elemento para la lista: "))
    lista.append(elemento)

    val = int(input("Desea agregar otro valor? 1- SI  2- NO: "))

    if val == 2:
        break


suma =sum(lista)


print(f"Lista: {lista}")
print(f"Suma: {suma}")


