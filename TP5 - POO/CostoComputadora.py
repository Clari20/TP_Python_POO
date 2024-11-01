

from Computadora import Computadora
from ComponenteCPU import ComponenteCPU

class CostoComputadora:
    def __init__(self):
        self.computadoras = []

    def agregar_computadora(self):
        marca = input("Ingrese la marca de la computadora: ")
        modelo = input("Ingrese el modelo de la computadora: ")
        computadora = Computadora(marca, modelo)

        while True:
            componente = input("Ingrese el nombre del componente: ")
            marca_componente = input("Ingrese la marca del componente: ")
            cantidad = int(input("Ingrese la cantidad del componente: "))
            precio = float(input("Ingrese el precio del componente: "))
            componente_cpu = ComponenteCPU(componente, marca_componente, cantidad, precio)
            computadora.agregar_componente(componente_cpu)

            mas_componentes = input("¿Desea agregar más componentes? (si/no): ").lower()
            if mas_componentes != 'si':
                break

        self.computadoras.append(computadora)

    def mostrar_computadoras(self):
        for computadora in self.computadoras:
            print(computadora)

    def main(self):
        while True:
            self.agregar_computadora()
            self.mostrar_computadoras()
            mas_computadoras = input("¿Desea cotizar una nueva computadora? (si/no): ").lower()
            if mas_computadoras != 'si':
                break

if __name__ == "__main__":
    costo_computadora = CostoComputadora()
    costo_computadora.main()
