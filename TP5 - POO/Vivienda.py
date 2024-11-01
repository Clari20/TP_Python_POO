

from Habitacion import Habitacion

class Vivienda:
    def __init__(self, calle, numero, manzana, nro_casa, superficie_terreno, habitaciones=None):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nro_casa = nro_casa
        self.superficie_terreno = superficie_terreno
        self.habitaciones = habitaciones if habitaciones is not None else []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def get_metros_cuadrados_cubiertos(self):
        metros_cuadrados_cubiertos = sum(habitacion.metros_cuadrados for habitacion in self.habitaciones)
        if metros_cuadrados_cubiertos > self.superficie_terreno:
            raise ValueError("La superficie cubierta no puede ser mayor a la superficie del terreno")
        return metros_cuadrados_cubiertos

    def __str__(self):
        info = f"Vivienda en {self.calle} {self.numero}, Manzana {self.manzana}, Casa {self.nro_casa}, Superficie Terreno: {self.superficie_terreno} m²\n"
        info += "Habitaciones:\n"
        for habitacion in self.habitaciones:
            info += f"{habitacion}\n"
        return info
