"""Cree una clase Fracción con dos atributos, numerador y denominador.
Agregue a la clase los siguientes 4 métodos e implemente los mismos:
sumarFracciones(Fraccion f1, Fraccion f2)
restarFracciones(Fraccion f1, Fraccion f2)
multiplicarFracciones(Fraccion f1, Fraccion f2)
dividirFracciones(Fraccion f1, Fraccion f2)
Todos los métodos deben retornar la fracción resultante de la operación.
Cree una clase OperacionesFraccion que contenga un método main donde se solicite
al usuario el ingreso de 4 valores numéricos enteros con los cuales se crearan 2 objetos
Fracción y finalizada la creación de los mismos se ejecutaran los 4 métodos
implementados anteriormente asignando el resultado a una nueva variable de tipo
Fracción y mostrando por pantalla el resultado de las operaciones realizadas.
"""

class Fraccion:

    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def sumarFracciones(self, f1, f2):
        nuevo_numerador = (f1.numerador * f2.denominador) + (f2.numerador * f1.denominador)
        nuevo_denominador = f1.denominador * f2.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def restarFracciones(self, f1, f2):
        nuevo_numerador = (f1.numerador * f2.denominador) - (f2.numerador * f1.denominador)
        nuevo_denominador = f1.denominador * f2.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def multiplicarFracciones(self, f1, f2):
        nuevo_numerador = f1.numerador * f2.numerador
        nuevo_denominador = f1.denominador * f2.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def dividirFracciones(self, f1, f2):
        if f2.numerador == 0:
            return "Error: División por cero"
        nuevo_numerador = f1.numerador * f2.denominador
        nuevo_denominador = f1.denominador * f2.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"



class OperacionesFraccion:
    def main():
        num1 = int(input("Ingrese el numerador 1: "))
        den1 = int(input("Ingrese el denominador 1: "))

        num2 = int(input("Ingrese el numerador 2: "))
        den2 = int(input("Ingrese el denominador 2: "))

        fraccion1 = Fraccion(num1, den1)
        fraccion2 = Fraccion(num2, den2)

        # Crear una instancia de Fraccion para realizar las operaciones
        operaciones = Fraccion(0, 1)

        # Sumar fracciones
        resultado_suma = operaciones.sumarFracciones(fraccion1, fraccion2)
        print(f"Resultado de la suma: {resultado_suma}")

        # Restar fracciones
        resultado_resta = operaciones.restarFracciones(fraccion1, fraccion2)
        print(f"Resultado de la resta: {resultado_resta}")

        # Multiplicar fracciones
        resultado_multiplicacion = operaciones.multiplicarFracciones(fraccion1, fraccion2)
        print(f"Resultado de la multiplicación: {resultado_multiplicacion}")

        # Dividir fracciones
        resultado_division = operaciones.dividirFracciones(fraccion1, fraccion2)
        print(f"Resultado de la división: {resultado_division}")


OperacionesFraccion.main()




