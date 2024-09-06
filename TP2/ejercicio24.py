"""Crea un programa que lea una cadena de texto carácter por carácter usando
recursión.
Ejemplo: Ingreso “UTN FRM Mza”
Salida: U
T
N
F
R
M
M
z
a"""

def leer_cadena(cadena, index=0):
    if index==len(cadena):
        return
    else: 
        print(cadena[index])
        leer_cadena(cadena,index+1)

cadena = input("Ingrese una cadena: ")
leer_cadena(cadena)