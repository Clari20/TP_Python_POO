"""Explique y ejemplifique la librería NumPy para trabajar con matrices y
arrays"""

#NumPy = Proporciona soporte para arrays y matrices de gran tamaño, 
#así como una colección de funciones matemáticas para operar sobre estos arrays.

#Algunas caracteristicas importantes de esta libreria son: 

# - Permite crear y manipular arrays de una o más dimensiones (escalares, vectores, matrices, tensores, etc.).
# - Presenta una amplia gama de funciones matemáticas que se pueden aplicar: suma, resta, multiplicación, división, raíz cuadrada, exponencial, logaritmo,etc


#Primero tenes que importar la libreria
import numpy as np

#Podes crear un array
print("Creamos un Array: ")
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#Sumar dos arrays distintos
print("Sumamos dos Arrays dando como resultado: ")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
suma = arr1 + arr2
print(suma)

#Y hacer operaciones mas complejas como sacar las raices cuadradas de un array
print("Calculamos las raices cuadradas de un array: ")
arr3 = np.array([1, 4, 9, 16])
raiz = np.sqrt(arr3)
print(raiz)
