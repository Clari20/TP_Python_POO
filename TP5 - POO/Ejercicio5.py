"""5. Codifique las siguientes clases Python en archivos diferentes
Clase: Barrio
Atributos: nombre (cadena), empresaConstructora (cadena), lista de objetos Vivienda[]
Clase: Vivienda
Atributos: calle (cadena), numero (entero), manzana (cadena), nroCasa (entero),
superficieTerreno (decimal), lista de objetos Habitacion []
Clase: Habitacion
Atributos: nombre (cadena), metrosCuadrados (decimal)
Codifique los siguientes métodos en las Clases indicadas
a) Codifique en la clase Barrio un método llamado
getSuperficieTotalTerreno()
que retorne el total de metros de terreno del barrio teniendo en cuenta la
totalidad de viviendas asociadas al mismo. Es decir deberá sumar el atributo
superficieTerreno de las viviendas asociadas.
b) Codifique en la clase Barrio un método llamado
getSuperficieTotalTerrenoXManzana(manzana)
que retorne el total de metros de terreno de una manzana especifica del barrio
teniendo en cuenta la totalidad de viviendas de esa manzana. Es decir deberá
sumar el atributo superficieTerreno de las viviendas asociadas filtrando por su
manzana.
c) Codifique en la clase Vivienda un método denominado
getMetrosCuadradosCubiertos()
que retorne el total de metros cuadrados de la vivienda teniendo en cuenta la
cantidad de habitaciones asociadas y sus respectivos metros cuadrados. Al finalizar
el cálculo valide que el valor obtenido no sea mayor que la superficie del terreno,
si ocurre esa situación emita una excepción con el mensaje “La superficie cubierta
no puede ser mayor a la superficie del terreno” 
Codifique en la clase Barrio un método llamado
getSuperficieTotalCubierta()
que retorne los metros cuadrados cubiertos del barrio sumando la totalidad de
metros cuadrados cubiertos de las viviendas que componen al barrio. Reutilice el
método getMetrosCuadradosCubiertos() del punto anterior.
e) Codifique una clase donde cree los objetos Barrio, Vivienda y Habitaciones, ejecute
las asociaciones correspondientes y muestre por pantalla el resultante de la
ejecución de los métodos codificados en los métodos anteriores"""