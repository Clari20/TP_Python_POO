"""Indique si en Python existen o no variables de tipo valor y su contraparte tipo
referencia como sucede en otros lenguajes como Java."""


#Las variables de tipo valor almacenan directamente el valor de los datos en la memoria.

#Ejemplos:
#En lenguajes como C, C++, y Java, los tipos de datos primitivos (como int, float, char, boolean, etc.) 
#Las modificaciones en una variable no afectan a la otra.

#En python lo mas cercano a las variables de tipo valor, son las variables tipo Inmutable, por ej:

a = 10
b = a
a = 20

print(a)  
print(b)  



#Las variables de tipo referencia (o mutable en Python) almacenan una referencia a la ubicación en la memoria donde se encuentran los datos.

#Ejemplos:
#En lenguajes como Java, los objetos (como String, List, Object, etc.) son variables de tipo referencia.
#En Python, todas las variables son referencias a objetos en memoria.
#Las modificaciones en una variable pueden afectar a la otra si ambas apuntan al mismo objeto

#Ejemplo de variable tipo Referencia: 

lista1 = [1, 2, 3]
lista2 = lista1
lista1.append(4)

print(lista1)  
print(lista2)  


#Una de las principales diferencias es que: 
#Tipos Inmutables(por valor): Modificaciones en una variable no afectan a la otra porque cada variable puede apuntar a un objeto diferente.
#Tipos Mutables(por referencia): Modificaciones en una variable pueden afectar a la otra si ambas variables apuntan al mismo objeto.


#Conclusion:
#En Python NO existen variables clasificadas por valor y por referencia, 
# lo mas cercano es variables mutables e inmutables (explicadas arriba)