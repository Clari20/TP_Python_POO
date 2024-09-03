"""Recorre la cadena del ejercicio 6 y transforma cada carácter a su código ASCII.
Muéstralos en línea recta, separados por un espacio entre cada carácter."""


cadena = str("La lluvia en Mendoza es escasa")

ascii = ' '.join(str(ord(caracter)) for caracter in cadena)

print(f"Si pasamos la frase ''{cadena}'' y cambiamos las letras por caracteres ASCII, esto se mostraría: ")
print(ascii)