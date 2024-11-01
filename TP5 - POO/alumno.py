

from nota import Nota

class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_promedio(self):
        if not self.notas:
            return 0
        total = sum(nota.notaExamen for nota in self.notas)
        return total / len(self.notas)

    def __repr__(self):
        return f"Alumno(nombreCompleto={self.nombreCompleto}, legajo={self.legajo}, notas={self.notas})"
