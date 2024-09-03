"""Pedir dos palabras por teclado, indicar si son iguales."""


pal1 = input("Ingrese una palabra: ")
pal2 = input("Ingrese otra palabra: ")


if pal1 == pal2:
    print(f"Las palabras '{pal1}' y '{pal2}' son IGUALES")
else:
    print("Las palabras no son iguales :(")
