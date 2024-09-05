"""Cree una clase OperacionMatematica con dos atributos valor1 y valor2 y un
atributo de nombre operación.
Agregue a la clase los siguientes 5 métodos e implemente la lógica correspondiente:
sumarNumeros()
restarNumeros()
multiplicarNumeros()
dividirNumeros()
El quinto método será el siguiente:
aplicarOperacion(operacion){
.......................
}
Cree una clase Calculo que contenga un método main, donde cree una instancia de la
clase OperacionMatematica, asigne 2 valores para las variables de la instancia y
ejecute la función aplicarOperacion, pasando como parámetro primero “+”, después “-
”, a continuación “*” y finalmente “/”. Muestre por pantalla el resultado de las
operaciones."""




class Operaciones:
    def sumarNumeros(valor1, valor2):
        return valor1 + valor2

    def restarNumeros(valor1, valor2):
        return valor1 - valor2

    def multiplicarNumeros(valor1, valor2):
        return valor1 * valor2

    def dividirNumeros(valor1, valor2):
        return valor1 / valor2





    def aplicarOperacion(valor1, valor2, operacion):
        if operacion == "+":
            return Operaciones.sumarNumeros(valor1, valor2)
        elif operacion == "-":
            return Operaciones.restarNumeros(valor1, valor2)
        elif operacion == "*":
            return Operaciones.multiplicarNumeros(valor1, valor2)
        elif operacion == "/":
            return Operaciones.dividirNumeros(valor1, valor2)
        else:
            return "Operación no válida"
        

class Calculo:
    @staticmethod
    def main():
        # Definir los valores
        valor1 = int(input("Ingrese un valor: "))
        valor2 = int(input("Ingrese un segundo valor: "))

        # Aplicar las operaciones y mostrar los resultados
        resultado_suma = Operaciones.aplicarOperacion(valor1, valor2, "+")
        print(f"Resultado de la suma: {resultado_suma}")

        resultado_resta = Operaciones.aplicarOperacion(valor1, valor2, "-")
        print(f"Resultado de la resta: {resultado_resta}")

        resultado_multiplicacion = Operaciones.aplicarOperacion(valor1, valor2, "*")
        print(f"Resultado de la multiplicación: {resultado_multiplicacion}")

        resultado_division = Operaciones.aplicarOperacion(valor1, valor2, "/")
        print(f"Resultado de la división: {resultado_division}")

Calculo.main()