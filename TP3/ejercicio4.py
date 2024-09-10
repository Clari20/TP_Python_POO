"""Escribe un programa que pida al usuario una lista de números y cuente cuántos de
ellos son pares y cuántos son impares."""


entrada = input("Ingrese una lista de números separados por espacios: ")


numeros = list(map(int, entrada.split()))

par = 0
impar = 0

# Contar pares e impares
for numero in numeros:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

# Mostrar el resultado
print(f"Números pares: {par}")
print(f"Números impares: {impar}")
