"""Reemplaza todas las vocales a de una cadena ingresada por teclado por una vocal e."""

cadena = str(input("Ingrese una frase u oracion: "))

nuev = cadena.replace('a', 'e').replace('A', 'E')

print(f"Si a la cadena ''{cadena}'' le cambiamos las vocales por E, queda: {nuev}")