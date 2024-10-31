"""fechaFactura de tipo cadena
 numeroFactura de tipo entero
 letraFactura de tipo cadena
 totalFactura de tipo decimal
 montoIva de tipo decimal
 clienteFactura de tipo cadena
 detallesFactura que será una Lista de 2 dimensiones de N filas por 5
columnas correspondientes a:
"""

fechaFactura = str
numeroFactura = int
letraFactura = str
totalFactura = float
montoIva = float
clienteFactura = str
detallesFactura = [["Codigo Articulo", "Nombre Articulo", "Cantidad", "Precio Unitario", "Subtotal"]]


detallesFactura = [["CódigoArticulo","NombreArticulo","Cantidad","PrecioUnitario","subTotal"],
                 [101,"Leche         ",0,250,0,],
                 [102,"Gaseosa       ",0,300,0,],
                 [103,"Fideos        ",0,150,0,],
                 [104,"Arroz         ",0,280,0,],
                 [105,"Vino          ",0,1200,0,],
                 [106,"Manteca       ",0,200,0,],
                 [107,"Lavandina     ",0,180,0,],
                 [108,"Detergente    ",0,460,0,],
                 [109,"Jabón en Polvo",0,960,0,],
                 [110,"Galletas      ",0,600,0]]


clientes = {20110425417: "Rodolfo Fernandez",
            30527419655: "Los Pollos Hnos",
            27289425478: "Andrea Pereira",
            33536549878: "Multimarca Repuestos",
            20291122568: "Luis Peric"}

"""Solicitar los datos de fecha factura, y número de factura y
asignarlos en los atributos correspondientes."""

fechaFactura = str(input("Ingrese la fecha de factura: (DD-MM-AAAA) "))
numeroFactura = int(input("Ingrese el numero de factura: "))

"""Solicitar el CUIT del cliente, si el cuit ingresado existe en el
diccionario de clientes, obtenga el valor correspondiente y asigne
el mismo en la variable clienteFactura, caso contrario asigne el
valor “Consumidor Final”. Valide que el cuit ingresado inicie con
20, 27, 30 o 33"""

cuit = int(input("Ingrese el CUIT del cliente: "))


cuit_str = str(cuit)
if cuit_str[:2] in ["20", "27", "30", "33"]:
    if cuit in clientes:
        clienteFactura = clientes[cuit]
    else:
        clienteFactura = "Consumidor Final"
else:
    clienteFactura = "CUIT no válido"


"""Solicitar el código del articulo a facturar, buscar el código en la
lista de artículos, si no se encuentra el código indicar la situación
con un mensaje “Código Incorrecto” y volver a pedir el código
nuevamente, si el código se encuentra solicitar la cantidad de
artículos a facturar y aplicar la información obtenida para cargar la
lista detallesFactura (contemple que el subtotal es el resultante de
multiplicar precio unitario por cantidad). Repetir este proceso
hasta que el código ingresado sea 0000."""

while True:
    cod = int(input("Ingrese el código del artículo que desea (0000 para finalizar): "))

    if cod == 0:
        break

    articulo_encontrado = None
    for articulo in detallesFactura[1:]:  # Saltar la primera fila que es el encabezado
        if articulo[0] == cod:
            articulo_encontrado = articulo
            break

    if articulo_encontrado is None:
        print("Código Incorrecto")
    else:
        cant = int(input(f"Ingrese la cantidad de {articulo_encontrado[1]} que desea: "))
        subtotal = articulo_encontrado[3] * cant
        articulo_encontrado[2] = cant
        articulo_encontrado[4] = subtotal



"""Codifique un método calcularTotal que devolverá un valor decimal
que se corresponderá con la suma de los subtotales calculados en
el paso anterior."""

calcularTotal = 0.0
for detalle in detallesFactura[1:]:  # Saltar la primera fila que es el encabezado
    calcularTotal += detalle[4]




"""El valor asignado en el atributo montoIva se corresponderá a 0
pesos en el caso de que el cuit del cliente buscado anteriormente
inicie con 20 o 27 o sea consumidor final. Si el cuit ingresado inicio
en 30 o 33 se asignara en montoIva el 21% del total de la factura
calculado en el paso anterior."""

if cuit_str[:2] in ["20", "27"]:
    montoIva = 0.0
elif cuit_str[:2] in ["30", "33"]:
    montoIva = calcularTotal * 0.21


"""El valor asignado en el atributo letraFactura se corresponderá a
letra B en el caso de que el cuit del cliente buscado anteriormente
inicie con 20 o 27 o sea consumidor final. Si el cuit ingresado inicio
en 30 o 33 se asignara la letra A."""

if cuit_str[:2] in ["20", "27"]:
    letraFactura = "B"
elif cuit_str[:2] in ["30", "33"]:
    letraFactura = "A"



"""Finalmente asigne en la variable totalFactura el monto total
calculado en el punto d + el monto de iva en caso de que la letra
de la factura sea B, caso contrario si la letra de la factura es A
asigne únicamente el monto calculado en el punto d, dado que en 
este caso el IVA es discriminado en la factura en la variable
montoIva. """


if letraFactura == "B":
    totalFactura = calcularTotal + montoIva
elif letraFactura == "A":
    totalFactura = calcularTotal

"""Finalmente imprima por pantalla la totalidad de los datos de la
factura mostrando los datos cargados de una forma similar a la
siguiente:""" 

print(f"Fecha: {fechaFactura}\n")
print(f"Numero: {numeroFactura}\n")
print(f"Letra factura: {letraFactura}\n")
print(f"Cliente: {clientes[cuit]}\n")
print(" - - - - - - - - - - - - - - - ")
for i in detallesFactura:
        print (i[0]," | ",i[1]," | ",i[2]," | ",i[3]," | ",i[4])
print(" - - - - - - - - - - - - - - - ")
print(f"IVA: {montoIva}")
print(f"TOTAL: {totalFactura}")
