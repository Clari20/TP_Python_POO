class FuncionesPrograma:
    @staticmethod
    def getFechaString(fecha):


#Referencias:

        dias = {
            '01': 'Uno', '02': 'Dos', '03': 'Tres', '04': 'Cuatro', '05': 'Cinco',
            '06': 'Seis', '07': 'Siete', '08': 'Ocho', '09': 'Nueve', '10': 'Diez',
            '11': 'Once', '12': 'Doce', '13': 'Trece', '14': 'Catorce', '15': 'Quince',
            '16': 'Dieciséis', '17': 'Diecisiete', '18': 'Dieciocho', '19': 'Diecinueve',
            '20': 'Veinte', '21': 'Veintiuno', '22': 'Veintidós', '23': 'Veintitrés',
            '24': 'Veinticuatro', '25': 'Veinticinco', '26': 'Veintiséis', '27': 'Veintisiete',
            '28': 'Veintiocho', '29': 'Veintinueve', '30': 'Treinta', '31': 'Treinta y uno'
        }

        meses = {
            '01': 'Enero', '02': 'Febrero', '03': 'Marzo', '04': 'Abril', '05': 'Mayo',
            '06': 'Junio', '07': 'Julio', '08': 'Agosto', '09': 'Septiembre', '10': 'Octubre',
            '11': 'Noviembre', '12': 'Diciembre'
        }

        unidades = {
            '0': '', '1': 'uno', '2': 'dos', '3': 'tres', '4': 'cuatro',
            '5': 'cinco', '6': 'seis', '7': 'siete', '8': 'ocho', '9': 'nueve'
        }

        decenas = {
            '1': 'dieci', '2': 'veinti', '3': 'treinta y ', '4': 'cuarenta y ',
            '5': 'cincuenta y ', '6': 'sesenta y ', '7': 'setenta y ', '8': 'ochenta y ',
            '9': 'noventa y '
        }

        centenas = {
            '1': 'ciento', '2': 'doscientos', '3': 'trescientos', '4': 'cuatrocientos',
            '5': 'quinientos', '6': 'seiscientos', '7': 'setecientos', '8': 'ochocientos',
            '9': 'novecientos'
        }

        mil = {
            '1': 'mil', '2': 'dos mil', '3': 'tres mil', '4': 'cuatro mil',
            '5': 'cinco mil', '6': 'seis mil', '7': 'siete mil', '8': 'ocho mil',
            '9': 'nueve mil'
        }

        dia, mes, año = fecha.split('/')

# Convertir el año a palabras
        año_palabras = []
#Averiguar si el año ingresado tiene 4 numeros

        if len(año) == 4:

            #Si el digito 1 es diferente de cero, se prosigue y se agrega a la lista
            if año[0] != '0':
                año_palabras.append(mil[año[0]])

            #Si el digito 2 es diferente de cero, se prosigue y se agrega a la lista
            if año[1] != '0':
                año_palabras.append(centenas[año[1]])

            #Si el digito 3 es diferente de cero, se prosigue y se agrega a la lista
            if año[2] != '0':
                if año[2] == '1' and año[3] != '0':
                    año_palabras.append(decenas[año[2]][:-3])
                else:
                    año_palabras.append(decenas[año[2]])

            #Si el digito 4 es diferente de cero, se prosigue y se agrega a la lista
            if año[3] != '0' or (año[2] == '1' and año[3] != '0'):
                año_palabras.append(unidades[año[3]])

        año_palabras = ' '.join(año_palabras)

        fecha_lineal = f"{dias[dia]} de {meses[mes]} de {año_palabras}"

        return fecha_lineal

#Probar:

class Principal:
    @staticmethod
    def main():
        fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
        fecha_lineal = FuncionesPrograma.getFechaString(fecha)
        print(fecha_lineal)


Principal.main()
