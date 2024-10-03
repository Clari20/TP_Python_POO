"""Dada la siguiente tupla: numeros = (1, 2, 2, 3, 4, 4, 4, 5) 
a) Cuenta cuántas veces aparece el número 4 en la tupla. 
b) Imprime el resultado. """

numeros = (1, 2, 2, 3, 4, 4, 4, 5)

cont = 0

for numero in numeros:
    if numero == 4:
        cont+=1


print(f"El numero 4 aparece {cont} veces")