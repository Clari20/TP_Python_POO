

class Nota:
    def __init__(self, catedra, notaExamen):
        self.catedra = catedra
        self.notaExamen = notaExamen

    def __repr__(self):
        return f"Nota(catedra={self.catedra}, notaExamen={self.notaExamen})"
