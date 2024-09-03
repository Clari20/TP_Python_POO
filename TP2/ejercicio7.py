"""Solicite el ingreso de una cadena y determine el tamaño de la misma y cuantas
vocales tiene en total."""

cadena = str(input("Ingrese una frase u oracion: "))

long = len(cadena)

vocales = "aeiouAEIOU"


cant = sum(cadena.count(vocal) for vocal in vocales)

print(f"En la frase ''{cadena}'' de {long} caracteres, las vocales aparecen {cant} veces")

