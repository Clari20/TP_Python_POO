"""Escribe un programa que pida al usuario una lista de números y encuentre el mayor y
el menor de ellos."""

lista = []

while True:
    elemento = int(input("Ingrese un elemento para la lista: "))
    lista.append(elemento)

    val = int(input("Desea agregar otro valor? 1- SI  2- NO: "))

    if val == 2:
        break

menor = min(lista)
mayor = max(lista)

print(lista)
print(f"El numero mayor de la lista es {mayor} y el menor es {menor}")