"""Escribe un programa que multiplique cada elemento de una lista de números por un
valor ingresado por el usuario."""


entrada = input("Ingrese una lista de números separados por espacios: ")


numeros = list(map(int, entrada.split()))

num2 = int(input("Ingrese el numero por el que quiere multiplicar: "))

while True:
    num3 = [numero * num2 for numero in numeros]
    
    print(num3)
    break