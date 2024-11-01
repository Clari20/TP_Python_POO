"""Codifique las siguientes clases Python en archivos diferentes
Clase: Ingrediente
Atributos: nombre (cadena), cantidad(decimal), unidad de medida (cadena)
Clase: Plato
Atributos: nombreCompleto(cadena), precio (decimal), esBebida (boolean), lista de
ingredientes[]
Clase: MenuRestaurant (clase que tendrá declarado el método main para ejecutar el
código.)
Lógica a Implementar:
En la clase MenuRestaurant debera declarar una variable “platosMenu[]” que permita
contener un conjunto de Platos que componen el menú de un restaurant.
Ejemplo:
platos = [];
El algoritmo debe permitir cargar N platos y para cada plato indicar los N ingredientes que
lo componen. Si el plato es de tipo Bebida entonces no se deben solicitar los ingredientes,
en cambio si no lo es, será obligatorio que se asigne al menos 1 ingrediente.
Al finalizar la carga de los platos y sus ingredientes mostrar la información cargada, la cual
será equivalente al menú del restaurant.
Descripción del algoritmo:
Solicito los datos del plato (Ejemplo Pizza Especial, 450 pesos) y sus ingredientes (harina
100 gramos, huevos 2 unidades, queso 300 gramos, jamón 100 gramos, etc) o si es una
bebida solo pido el nombre y el precio.
Almaceno el plato anterior en la lista de platos “platosMenu[]”, repito este proceso para
tantos platos como desee. Al finalizar muestro la información respetando el siguiente
formato ejemplo
-----------MENÚ----------------
Pizza Especial
Precio: $ 450
Ingredientes:
Nombre Cantidad Unidad de Medida
Queso Muzza300 gramos
Jamon Cocido 100 gramos
----------------------------------
Vino Tinto Elementos
Precio: $ 300
----------------------------------
Empanadas Criollas
Precio: $ 500
Ingredientes:
Nombre Cantidad Unidad de Medida
Picadillo 150 gramos
Tapa Empanada 1 unidad
---------------------------------
…..repetir…..para el resto de los platos"""

