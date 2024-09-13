"""Escribe un programa que permita al usuario ingresar una lista de números y eliminar
un elemento en un índice especificado."""

entrada = input("Ingrese una lista de números separados por espacios:")

lista = list(map(int, entrada.split()))

num = int(input("Ingrese el indice del valor que desea eliminar: "))

eliminar = lista.pop(num)
print(f"La lista sin el valor ubicado en el indice {num} es : {lista}") 
