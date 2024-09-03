"""Pedir el ingreso de dos cadenas por por teclado, indicar si la segunda cadena se
encuentra dentro de la primera."""

cad1 = str(input("Ingrese una frase: "))
cad2= str(input("Ingrese una segunda cadena: "))

if cad1 in cad2:
    print(f"La cadena ''{cad1}'' SI esta dentro de la cadena ''{cad2}''")

elif cad2 in cad1:
    print(f"La cadena ''{cad2}'' SI esta dentro de la cadena ''{cad1}''")

else: 
    print("Ninguna de las dos cadenas esta dentro de la otra")