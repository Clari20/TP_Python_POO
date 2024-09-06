"""Codifique un programa que solicite un número entero mayor a cero y que
mediante recursión sume todos los números números naturales desde el número
ingresado hasta 1.
Ejemplo: Ingreso 10
El programa debe sumar 10 + 9 + 8 +7 +6 + 5 + 4 + 3 + 2 + 1"""

num = int(input("Ingrese un numero mayor a cero: "))


if num <= 0:
    print("El numero ingresado no es valido")

else:
    suma = 0
    while num > 0:
        suma += num
        print(num, end="")
        if num > 1:
            print(" + ", end="")
        num -= 1