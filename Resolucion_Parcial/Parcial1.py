"""Codifique la siguiente Lista de 2 dimensiones “golosinas”, que se corresponde a
una máquina expendedora de golosinas donde la columna 0 es el código de la
golosina, la columna 1 es la golosina, y la columna 2 es la cantidad (stock) actual de
golosinas 5%"""


golosinas = [
    [1, "KitKat", 20],
    [2, "Chicles", 50],
    [3, "Caramelos de Menta", 50],
    [4, "Huevo Kinder", 10],
    [5, "Chetoos", 10],
    [6, "Twix", 10],
    [7, "M&MS", 10],
    [8, "Papas Lays", 2],
    [9, "Milkybar", 10],
    [10, "Alfajor Tofi", 15],
    [11, "Lata Coca", 20],
    [12, "Chitos", 10]
]

"""Codifique un Diccionario “empleados” donde el par clave valor, representa al
legajo de un empleado y a su nombre 5%
"""

empleados = {
    1100: "José Alonso",
    1200: "Federico Pacheco",
    1300: "Nelson Pereira",
    1400: "Osvaldo Tejada",
    1500: "Gastón Garcia"
}

"""Codifique una Tupla “clavesTecnico” que contendrá 3 palabras que servirán como
clave de desbloqueo para el técnico que da mantenimiento a la máquina de
golosinas 2.5%"""

clavesTecnico = ("admin", "CCCDDD", 2020)

"""Finalmente tendremos una variable “golosinasPedidas” que será una Lista de N
filas por 3 columnas, donde guardaremos el historial de golosinas pedidas por los
empleados, donde las columnas se corresponderán a: 2.5%
"""

golosinasPedidas = [["Código golosina", "Denominación Golosina", "Cantidad total pedida"]]


"""Pedir golosina: Si se selecciona esta opción la maquina solicitara el ingreso
del legajo del empleado para validar que sea parte de la empresa y puede
acceder a las golosinas de forma gratuita, si el legajo ingresado no se
encuentra en el diccionario, deberá emitir el mensaje “Usted no es un
empleado de la empresa”, caso contrario si el legajo es correcto se pedirá el
código de la golosina que quiera. Esta máquina tiene golosinas en cada fila,
identificados por su código, por ejemplo si el usuario teclea 2 significa que
está pidiendo Chicles. Al seleccionar una golosina debe disminuir la cantidad
disponible de la golosina. En caso de agotar el stock de la golosina deberá
informar de la situación al cliente emitiendo el mensaje “Lo sentimos la
golosina XXXXX no se encuentra disponible, seleccione otra golosina o
ingresa salir si no desea otra golosina”. Por lo que el empleado tendrá esas 2
posibilidades para ejecutar. En el caso de que la golosina si posea stock
además de descontar la cantidad actual de la misma deberá registrar la
golosina extraída de la maquina en la lista “golosinasPedidas” donde la
cantidad total pedida se incrementara en 1 cada vez que se pida esa
golosina, no pudiendo existir más de 1 fila por cada golosina. Finalizada la
ejecución de esta funcionalidad se debe retornar al menú. 35%"""



def pedir_golosina():
    legajo = int(input("Ingrese el legajo: "))

    
    if legajo in empleados:
        cod = int(input("Ingrese el código de la golosina que desea: "))

        # Verificar si el código de la golosina existe
        golosina_encontrada = False
        for golosina in golosinas:

            # Golosina encontrada
            if golosina[0] == cod:
                golosina_encontrada = True

                # Verificar si la golosina está disponible
                while golosina[2] == 0:
                    print(f"Lo sentimos, la golosina {golosina[1]} no se encuentra disponible. Seleccione otra golosina o ingrese 'salir' si no desea otra golosina.")
                    print("Intente otra vez...")
                    cod = input("Ingrese el código de la golosina que desea: ")
                    if cod.lower() == "salir":
                        return
                    cod = int(cod)

                    for golosina in golosinas:
                        if golosina[0] == cod:
                            golosina_encontrada = True
                            break
                    if not golosina_encontrada:
                        print("Código de golosina no válido.")
                        return
                    
                if golosina[2] > 0:
                    golosina[2] -= 1
                    # Verificar si la golosina ya está en la lista de pedidas
                    for pedida in golosinasPedidas:
                        if pedida[0] == golosina[0]:
                            pedida[2] += 1
                            break
                    else:
                        golosinasPedidas.append([golosina[0], golosina[1], 1])
                break
        if not golosina_encontrada:
            print("Código de golosina no válido.")

    else:
        print("Usted no es un empleado de la empresa.")

# Ejecutar la función para pedir una golosina
pedir_golosina()

# Imprimir las golosinas pedidas
print("Golosinas pedidas:")
for pedida in golosinasPedidas:
    print(pedida  )


"""Mostrar golosinas: mostrara todas las golosinas con la cantidad actual
disponible, sin la necesidad de ingresar legajo o clave alguna. Finalizada la
ejecución de esta funcionalidad se debe retornar al menú. 10%"""

print(golosinas)

"""Rellenar golosinas: esta es una función exclusiva de un técnico por lo que
para su ejecución nos pedirá una contraseña de 3 pasos, si el usuario escribe
las 3 palabras asignadas en la Tupla “clavesTecnico” respetando el mismo
orden indicado, nos autorizara y pedirá el código de la golosina, si el código
es correcto, se pedirá la cantidad a recargar, donde la mima debe ser mayor
a cero. La cantidad ingresada se sumara a la cantidad actual existente. Si la
clave ingresada no es válida emitirá el mensaje “No tiene permiso para
ejecutar la función de recarga”. Finalizada la ejecución de esta
funcionalidad se debe retornar al menú. 25%"""

def claves():


    #clavesTecnico = ("admin", "CCCDDD", "2020")

    # Clave 1
    clave1 = str(input("Ingrese el str de la clave 1: "))
    while clave1 != "admin":
        print("No tiene permiso para ejecutar la función de recarga")
        clave1 = str(input("Ingrese el str de la clave 1: "))
        break
    if clave1 == "admin":

        # Clave 2

        clave2 = str(input("Ingrese las letras de la clave 2: "))
        while clave2 != "CCCDDD":
            print("No tiene permiso para ejecutar la función de recarga")
            clave2 = str(input("Ingrese el str de la clave 2: "))
            break
        if clave2 == "CCCDDD":

            # Clave 3

            clave3 = int(input("Ingrese los numeros de la clave 3: "))
            while clave3 != 2020:
                print("No tiene permiso para ejecutar la función de recarga")
                clave3 = int(input("Ingrese el str de la clave 3: "))
                break

            if clave3 == 2020:

                # Entra

                print("Felicitaciones, ingresaste")

                # Reponer golosina
                
                codgolosina = int(input("Ingrese el codigo de la golosina: "))
                
                golosina_encontrada = False
                for golosina in golosinas:
                    if golosina[0] == codgolosina:
                        golosina_encontrada = True
                        cantgolosina = int(input("Ingrese la cantidad que desea reponer: "))

                        if cantgolosina < 0:
                            print("Inválido. El número debe ser mayor a cero.")
                        else:
                            golosina[2] += cantgolosina
                            print(f"La golosina {golosina[1]} ha sido repuesta. Nueva cantidad: {golosina[2]}")
                        break

                    
                



claves()
print("\n")
print(golosinas)

"""Apagar maquina: sale del programa, antes de salir mostrara la lista
“golosinasPedidas” listando todas las golosinas pedidas durante la ejecución
del programa. Indicando también como dato final el total de golosinas
pedidas, es decir la suma de la columna cantidad total pedida. 15%"""

apagar = input("Desea apagar la máquina? Si = 'S'  No = 'N' ")
mayuscula = apagar.upper()
while mayuscula != "S":
    sumagolosina = 0
    print(golosinasPedidas)
    for golosina in golosinasPedidas:
        if isinstance(golosina[2], int):  
            sumagolosina += golosina[2]

    print(f"El total de golosinas pedidas es: {sumagolosina}")

    apagar = input("Desea apagar la máquina? Si = 'S'  No = 'N' ")
    mayuscula = apagar.upper()
print("Adios...")







