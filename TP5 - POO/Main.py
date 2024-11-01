

from Barrio import Barrio
from Vivienda import Vivienda
from Habitacion import Habitacion

def main():
    # Crear habitaciones
    habitacion1 = Habitacion("Sala", 50)
    habitacion2 = Habitacion("Cocina", 20)
    habitacion3 = Habitacion("Dormitorio", 30)

    # Crear viviendas
    vivienda1 = Vivienda("Calle A", 1, "A", 1, 200)
    vivienda1.agregar_habitacion(habitacion1)
    vivienda1.agregar_habitacion(habitacion2)

    vivienda2 = Vivienda("Calle B", 2, "B", 2, 150)
    vivienda2.agregar_habitacion(habitacion3)

    # Crear barrio
    barrio = Barrio("Barrio Nuevo", "Constructora XYZ")
    barrio.agregar_vivienda(vivienda1)
    barrio.agregar_vivienda(vivienda2)

    # Mostrar información del barrio
    print(barrio)

    # Mostrar superficie total de terreno del barrio
    print(f"Superficie total de terreno del barrio: {barrio.get_superficie_total_terreno()} m²")

    # Mostrar superficie total de terreno de una manzana específica
    manzana = "A"
    print(f"Superficie total de terreno de la manzana {manzana}: {barrio.get_superficie_total_terreno_x_manzana(manzana)} m²")

    # Mostrar superficie total cubierta del barrio
    print(f"Superficie total cubierta del barrio: {barrio.get_superficie_total_cubierta()} m²")

if __name__ == "__main__":
    main()
