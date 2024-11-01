

from alumno import Alumno
from nota import Nota

class CargaNotas:
    def __init__(self):
        self.alumnos = []

    def main(self):
        while True:
            print("INGRESE DATOS DEL ALUMNO")
            nombreCompleto = input("INGRESE NOMBRE COMPLETO: ")
            legajo = int(input("INGRESE LEGAJO: "))
            alumno = Alumno(nombreCompleto, legajo)

            while True:
                catedra = input("INGRESE NOMBRE CATEDRA: ")
                notaExamen = float(input("Nota: "))
                nota = Nota(catedra, notaExamen)
                alumno.agregar_nota(nota)

                salirNotas = input("DESEA SALIR DE LA CARGA DE NOTAS (S/N): ").upper()
                if salirNotas == 'S':
                    break

            self.alumnos.append(alumno)

            salirAlumno = input("DESEA SALIR DE CARGA DE ALUMNOS (S/N): ").upper()
            if salirAlumno == 'S':
                break

        for alumno in self.alumnos:
            print(f"Datos Alumno: {alumno.nombreCompleto}, Legajo: {alumno.legajo}")
            for nota in alumno.notas:
                print(f"Nota: {nota.catedra}, {nota.notaExamen}")
            print(f"El promedio del alumno es: {alumno.calcular_promedio()}")

if __name__ == "__main__":
    carga_notas = CargaNotas()
    carga_notas.main()
