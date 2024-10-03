"""Dado el siguiente texto: texto = "manzana naranja manzana pera pera pera naranja manzana" 
a) Escribe un programa que cuente cuántas veces aparece cada palabra en el texto utilizando un diccionario. 
b) Imprime el diccionario resultante."""


texto = "manzana naranja manzana pera pera pera naranja manzana"


conteo = {}


palabras = texto.split()


for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1


print(conteo)
