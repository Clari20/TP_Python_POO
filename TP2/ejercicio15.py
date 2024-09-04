"""Indique que sucede si realizo la siguiente declaración de variable:
x = None print(x)
Explique y ejemplifique el uso de None"""

x = None 

print(x)

#None, representa la ausencia de un valor o un valor nulo
#Útil cuando necesitas indicar que una variable no tiene un valor asignado o que una función no devuelve un valor significativo.



valor = None

if valor is None:
    print("La variable 'valor' es None")
else:
    print("La variable 'valor' tiene un valor asignado")

valor = 10


if valor is None:
    print("La variable 'valor' es None")
else:
    print(f"La variable 'valor' tiene un valor asignado y es {valor}")




