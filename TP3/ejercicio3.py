"""Escribe un programa que permita al usuario ingresar una lista y la invierta."""

lista = []

while True:
    elemento = int(input("Ingrese un elemento para la lista: "))
    lista.append(elemento)

    val = int(input("Desea agregar otro valor? 1- SI  2- NO: "))

    if val == 2:
        break


print(f"la lista es: {lista}")


lista.reverse()


print(f"la lista al revés es: {lista}")