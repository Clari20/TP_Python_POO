
class Habitacion:
    def __init__(self, nombre, metros_cuadrados):
        self.nombre = nombre
        self.metros_cuadrados = metros_cuadrados

    def __str__(self):
        return f"{self.nombre} - {self.metros_cuadrados} m²"
