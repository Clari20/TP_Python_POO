from ComponenteCPU import ComponenteCPU

class Computadora:
    def __init__(self, marca, modelo, componentes=None):
        self.marca = marca
        self.modelo = modelo
        self.componentes = componentes if componentes is not None else []

    def agregar_componente(self, componente):
        self.componentes.append(componente)

    def costo_total(self):
        return sum(componente.subtotal() for componente in self.componentes)

    def precio_sugerido(self):
        costo = self.costo_total()
        if costo < 50000:
            return costo + (0.40 * costo)
        else:
            return costo + (0.30 * costo)

    def __str__(self):
        info = f"-----------Computadora----------------\n"
        info += f"Marca: {self.marca}\n"
        info += f"Modelo: {self.modelo}\n"
        info += "Componentes:\n"
        info += "Componente Marca Cantidad Precio X Unidad SubTotal\n"
        for componente in self.componentes:
            info += f"{componente}\n"
        info += f"Costo Total {self.costo_total()}\n"
        info += f"El precio sugerido de venta es {self.costo_total()} + {self.precio_sugerido() - self.costo_total()} = {self.precio_sugerido()}\n"
        return info
