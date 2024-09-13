"""Escribe un programa que sume dos listas de números elemento por elemento. Las
listas deben tener la misma longitud."""

entrada1 = input("Ingrese una lista de números separados por espacios:")
lista1 = list(map(int, entrada1.split()))

entrada2 = input("Ingrese una segunda lista de números separados por espacios:")
lista2 = list(map(int, entrada2.split()))

long1 = len(lista1)
long2 = len(lista2)

if long1 == long2:
    suma = sum(lista1)
    suma2 = sum(lista2)
    sumafinal = suma + suma2
    print("Las listas son igual de largas")
    print(f"La suma de la lista 1 es ''{suma}'', la suma de la lista 2 es ''{suma2}'' y la suma de ellas es: {sumafinal}")

else: 
    print("Las listas NO son igual de largas, reinicie el proceso")
