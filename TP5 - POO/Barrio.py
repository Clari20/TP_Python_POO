

from Vivienda import Vivienda

class Barrio:
    def __init__(self, nombre, empresa_constructora, viviendas=None):
        self.nombre = nombre
        self.empresa_constructora = empresa_constructora
        self.viviendas = viviendas if viviendas is not None else []

    def agregar_vivienda(self, vivienda):
        self.viviendas.append(vivienda)

    def get_superficie_total_terreno(self):
        return sum(vivienda.superficie_terreno for vivienda in self.viviendas)

    def get_superficie_total_terreno_x_manzana(self, manzana):
        return sum(vivienda.superficie_terreno for vivienda in self.viviendas if vivienda.manzana == manzana)

    def get_superficie_total_cubierta(self):
        return sum(vivienda.get_metros_cuadrados_cubiertos() for vivienda in self.viviendas)

    def __str__(self):
        info = f"Barrio: {self.nombre}, Empresa Constructora: {self.empresa_constructora}\n"
        info += "Viviendas:\n"
        for vivienda in self.viviendas:
            info += f"{vivienda}\n"
        return info
