"""Convertir una cadena a mayúsculas o minúsculas, daremos opción a que el usuario
pida que se desea hacer (convertir a mayúsculas o convertir a minúsculas) y mostrar el
resultado por pantalla."""

cadena = str(input("Ingrese una frase: "))

num = int(input("Ingrese 1 si quiere pasar su frase a mayusculas. Ingrese 2 si desea pasar su frase a minusculas: "))

if num == 1: 
    print(cadena.upper())

elif num == 2:
    print(cadena.lower())

else: 
    print("El numero que ingresó no es valido")

