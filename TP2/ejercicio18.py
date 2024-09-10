"""En la clase FuncionesPrograma codifique una método getFechaDate estática que
reciba como parámetro 3 valores enteros, día, mes, anio y retorne la fecha de tipo
date correspondiente.
En la clase Principal creada en el punto anterior haga uso de la función getFechaDate."""


from num2words import num2words
from datetime import datetime, date
import locale

# Establecer la configuración regional a español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

valid = False

while not valid:
    fechamanual = input("Ingrese una fecha con el siguiente formato 02-09-2024: ")
    # El bloque try se utiliza para manejar excepciones, es decir, errores que pueden ocurrir durante la ejecución de un programa.
    try:
        fechavalida = datetime.strptime(fechamanual, "%d-%m-%Y")
        valid = True
    except ValueError:
        print("Formato de fecha incorrecto. Intente de nuevo.")

class FuncionesPrograma:
    @staticmethod
    def getFechaDate(dia, mes, anio):
        # Crear una fecha de tipo date
        fecha = date(anio, mes, dia)
        return fecha

    @staticmethod
    def fechaLiteral(fecha):
        # Transformar los números a palabras
        dia = num2words(fecha.day, lang='es')
        mes = fecha.strftime("%B")
        anio = num2words(fecha.year, lang='es')
        fechaliteral = f"{dia} de {mes} del {anio}"
        return fechaliteral

class Principal:
    def main(self, fechavalida):
        dia = fechavalida.day
        mes = fechavalida.month
        anio = fechavalida.year
        fecha = FuncionesPrograma.getFechaDate(dia, mes, anio)
        fechaliteral = FuncionesPrograma.fechaLiteral(fecha)
        print(fechaliteral)

principal = Principal()
principal.main(fechavalida)
