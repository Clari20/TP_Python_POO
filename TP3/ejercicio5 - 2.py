"""Escribe un programa que encuentre el valor más grande en una lista bidimensional."""


filas = int(input("Ingrese la cantidad de filas: "))
col = int(input("Ingrese la cantidad de columnas: "))


matriz = []


for i in range(filas):
    entrada = input(f"Ingrese los valores de la fila {i + 1} separados por espacios: ")
    fila = list(map(int, entrada.split()))
    if len(fila) != col:
        print(f"Error: La fila {i + 1} debe tener {col} elementos.")
        exit()
    matriz.append(fila)


print("La matriz ingresada es:")
for fila in matriz:
    print(fila)


maximo = max(max(fila) for fila in matriz)
minimo = min(min(fila) for fila in matriz)


print (f"El numero mayor es: {maximo}")
print (f"El numero menor es: {minimo}")

