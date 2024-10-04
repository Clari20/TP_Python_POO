"""
1.Mostrar todos los productos disponibles. 
2. Buscar un producto por su código. 
3. Modificar el precio de un producto. 
4. Eliminar un producto del inventario. 
5. Mostrar todos los productos cuyo precio esté en un rango dado por el usuario.

Crear un diccionario que contenga el inventario inicial con al menos 5 productos. 
- Cada clave será un código de producto (ej. "A001", "A002"). 
- Cada valor será una tupla con la descripción del producto y su precio. 

2. Implementar las siguientes funciones: 
- mostrar_inventario(inventario): 
Muestra todos los productos del inventario con su código, descripción y precio.
buscar_producto(inventario, codigo): Busca un producto por su código. 
Si existe, muestra su descripción y precio. 
- modificar_precio(inventario, codigo, nuevo_precio): 
Modifica el precio de un producto dado su código. 
- eliminar_producto(inventario, codigo): 
Elimina un producto del inventario usando su código. 
- productos_por_rango_de_precio(inventario, min_precio, max_precio): 
Muestra todos los productos cuyo precio esté entre min_precio y max_precio.  """

#DICCIONARIO

inv = {"A1": ("Manzana", 500),
       "A2": ("Desodorante", 1500),
       "A3": ("Pantalon", 21000),
       "A4": ("Plasticola", 2000),
       "A5": ("Lapicera", 1000)}



#Mostrar inv

def mostrar_inventario(inv):
    print(inv)

mostrar_inventario(inv)


#Buscar cod

codigo = input("Ingrese el codigo del producto que desea buscar: ")

def buscar_producto(inv, codigo):
    if codigo in inv:
        descripcion, precio = inv[codigo]
        print(f"Código: {codigo}")
        print(f"Descripción: {descripcion}")
        print(f"Precio: {precio}")
    else:
        print(f"El producto con código {codigo} no existe en el inventario.")

buscar_producto(inv, codigo)

#Cambiar precio

nuevo_precio = input("Ingrese el nuevo precio que le quiere colocar al producto: ")
def modificar_precio(inv, codigo, nuevo_precio):
    

    if codigo in inv:
        descripcion, _ = inv[codigo]  
        inv[codigo] = (descripcion, nuevo_precio) 
        print(f"El precio del producto {codigo} ha sido actualizado a {nuevo_precio}.")
        print(inv)
    else:
        print(f"El producto con código {codigo} no existe en el inventario.")

modificar_precio(inv, codigo, nuevo_precio)



#Eliminar codigo

codigo2 =input("Ingrese el codigo del articulo que desea eliminar: ")
def eliminar_producto(inv, codigo2):
    del inv[codigo2]
    print(inv)

eliminar_producto(inv, codigo2)


#Min y Max

min = int(input("Ingrese el precio mínimo: "))
max = int(input("Ingrese el precio máximo: "))

def productos_por_rango_de_precio(inv, min, max):
    for codigo3, (descripcion, precio) in inv.items():
        if min <= precio <= max:
            print(f"{codigo3}\t{descripcion}\t{precio}")

productos_por_rango_de_precio(inv, min, max)





