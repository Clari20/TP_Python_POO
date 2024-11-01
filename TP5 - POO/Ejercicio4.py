"""Codifique las siguientes clases Python en archivos diferentes
Clase: ComponenteCPU
Atributos: componente (cadena), marca (cadena), cantidad (entero), precio (decimal)
Clase: Computadora
Atributos: marca(cadena), modelo (cadena), lista de objetos componenteCPU []
Clase: CostoComputadora (clase que tendrá declarado el método main para ejecutar el
código.)
Lógica a Implementar:
El algoritmo debe permitir cargar la marca y el modelo de una computadora y para cada
computadora indicar los N componentes de CPU que posee indicando la cantidad y el
precio por ejemplo componente “Memoria RAM 2 Gb”, marca “Kingston”, cantidad “2”,
precio “8000”
Al finalizar la carga de los componentes mostrar la información cargada, y determinar el
costo de la computadora el cual será el equivalente de sumar el precio por la cantidad
usada de cada componente y el precio de venta sugerido para la computadora el cual será
equivalente a el precio de costo más el 40% del precio de costo si el precio de costo es
menor a 50000, o equivalente a el precio de costo más el 30% del precio de costo si el
precio de costo es mayor a 50000.
Al terminar de mostrar los datos y precio de la computadora deberá preguntar si desea
cotizar una nueva computadora, si la respuesta es “SI” deberá iniciar nuevamente el
programa, si la respuesta es “NO”, terminar la ejecución del programa.
-----------Computadora----------------
Marca: Lenovo
Modelo: X64K
Componentes:
Componente Marca Cantidad Precio X Unidad SubTotal
Placa Madre ASUS 1 16000 16000
Procesador INTEL I7 1 20000 20000
Memoria RAM 2Gb Kingston 2 8000 16000
Disco Rigido WD SSD 1 7500 7500
Costo Total 59500
El precio sugerido de venta es 59500 + 17850 = 77350
"""