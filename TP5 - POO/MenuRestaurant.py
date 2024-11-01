

from Plato import Plato
from Ingrediente import Ingrediente

class MenuRestaurant:
    def __init__(self):
        self.platos_menu = []

    def agregar_plato(self):
        nombre_completo = input("Ingrese el nombre del plato: ")
        precio = float(input("Ingrese el precio del plato: "))
        es_bebida = input("¿Es una bebida? (si/no): ").lower() == 'si'

        plato = Plato(nombre_completo, precio, es_bebida)

        if not es_bebida:
            while True:
                nombre_ingrediente = input("Ingrese el nombre del ingrediente: ")
                cantidad = float(input("Ingrese la cantidad del ingrediente: "))
                unidad_medida = input("Ingrese la unidad de medida del ingrediente: ")
                ingrediente = Ingrediente(nombre_ingrediente, cantidad, unidad_medida)
                plato.agregar_ingrediente(ingrediente)

                mas_ingredientes = input("¿Desea agregar más ingredientes? (si/no): ").lower()
                if mas_ingredientes != 'si':
                    break

        self.platos_menu.append(plato)

    def mostrar_menu(self):
        print("-----------MENÚ----------------")
        for plato in self.platos_menu:
            print(plato)
            print("----------------------------------")

    def main(self):
        while True:
            self.agregar_plato()
            mas_platos = input("¿Desea agregar más platos? (si/no): ").lower()
            if mas_platos != 'si':
                break

        self.mostrar_menu()

if __name__ == "__main__":
    menu = MenuRestaurant()
    menu.main()
