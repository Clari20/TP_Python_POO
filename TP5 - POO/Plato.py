
from Ingrediente import Ingrediente

class Plato:
    def __init__(self, nombre_completo, precio, es_bebida, ingredientes=None):
        self.nombre_completo = nombre_completo
        self.precio = precio
        self.es_bebida = es_bebida
        self.ingredientes = ingredientes if ingredientes is not None else []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def __str__(self):
        info = f"{self.nombre_completo}\nPrecio: $ {self.precio}\n"
        if not self.es_bebida:
            info += "Ingredientes:\n"
            info += "Nombre Cantidad Unidad de Medida\n"
            for ingrediente in self.ingredientes:
                info += f"{ingrediente}\n"
        return info
