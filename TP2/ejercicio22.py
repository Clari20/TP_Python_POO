"""Suma los dígitos de un número ingresado por el usuario de forma recursiva.
Ejemplo: el usuario ingresa 1596
El programa debe sumar 1 + 5 + 9 + 6"""

num = int(input("Ingrese un numero de mas de una cifra: "))

suma = sum(int(digito) for digito in str(num))

print (f"El numero ingresado es {num}, la suma de los digitos es: {suma}")