"""Codifique la clase celda con los atributos:
fila; //entero
columna; //entero
valor; //cadena
 Crea una clase Matriz que contenga una variable celdas
celdasMatriz = [];
 Codifique un programa que solicite al usuario un valor para la celda y que solicite la
posición donde se desea almacenar el valor, cree una instancia de la clase Celda,
asigne los valores cargados por el usuario (fila, columna y valor) y agregue la
instancia a la lista celdasMatriz; repita este proceso hasta que el usuario ingrese
como valor la cadena “FIN”. Valide que la celda creada ya no exista anteriormente
es decir si la fila y columna indicados ya fueron cargados en celdasMatriz.
 Muestre por pantalla los valores cargados en la lista celdas.
 Codifique un método que reciba como parámetro los valores fila y columna y
retorne el valor almacenado en la Celda correspondiente, en caso de que la fila y la
columna no exista retorne el mensaje “La fila y columna indicada no ha sido
asignada en ninguna celda”"""


class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor

    def __repr__(self):
        return f"Celda(fila={self.fila}, columna={self.columna}, valor={self.valor})"


class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregar_celda(self, celda):
        for c in self.celdasMatriz:
            if c.fila == celda.fila and c.columna == celda.columna:
                print(f"La celda en la fila {celda.fila} y columna {celda.columna} ya existe.")
                return
        self.celdasMatriz.append(celda)

    def obtener_valor(self, fila, columna):
        for c in self.celdasMatriz:
            if c.fila == fila and c.columna == columna:
                return c.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"

    def mostrar_celdas(self):
        for celda in self.celdasMatriz:
            print(celda)


def main():
    matriz = Matriz()

    while True:
        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))
        valor = input("Ingrese el valor (o 'FIN' para terminar): ")

        if valor == "FIN":
            break

        celda = Celda(fila, columna, valor)
        matriz.agregar_celda(celda)

    print("Valores cargados en la matriz:")
    matriz.mostrar_celdas()

    fila = int(input("Ingrese la fila para obtener el valor: "))
    columna = int(input("Ingrese la columna para obtener el valor: "))
    valor = matriz.obtener_valor(fila, columna)
    print(f"El valor en la fila {fila} y columna {columna} es: {valor}")


main()


