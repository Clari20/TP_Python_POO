"""Desarrolle un programa que ayude a una cajera a determinar el número de billetes y
monedas que se necesitan de cada una de las siguientes denominaciones 200, 100, 50,
20, 10, 5, 2 y 1, y monedas de 0.50, 0.25, 0.10 y 0.05 centavos para una cantidad de
dinero dada. Ejemplo si la cantidad es 1390,55 se necesitan 6 billetes de 200, 1 billete
de 100, 1 billete de 50, 2 billetes de 20, 1 moneda de 0.50 y una moneda de 0.05
centavos. Plantee el algoritmo planteando métodos para su resolución."""

pago = float(input("Ingrese cuanto dinero debe pagar: "))


def calcular_billetes_y_monedas(pago):
    # Denominaciones de billetes y monedas
    billetes = [200, 100, 50, 20, 10, 5, 2, 1]
    monedas = [0.50, 0.25, 0.10, 0.05, 0.01]
    resultado = {}

    # Separar la parte entera y la parte decimal
    parte_entera = int(pago)
    parte_decimal = int(round(pago * 100)) % 100

    # Calcular billetes
    for billete in billetes:
        if parte_entera >= billete:
            resultado[billete] = parte_entera // billete
            parte_entera %= billete

    # Calcular monedas
    for moneda in monedas:
        if parte_decimal >= int(moneda * 100):
            resultado[moneda] = parte_decimal // int(moneda * 100)
            parte_decimal %= int(moneda * 100)

    return resultado

resultado = calcular_billetes_y_monedas(pago)

# Imprimir el resultado
print(f"Para la cantidad de {pago}:")
for denominacion, pago in resultado.items():
    if pago > 0:
        print(f"{pago} {'billetes' if denominacion >= 1 else 'monedas'} de {denominacion}")
