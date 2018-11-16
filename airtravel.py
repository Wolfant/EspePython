""" Modelo para vuelo de aviones"""


class Vuelo:

    def __init__(self, numero, aeronave):
        if not numero[:2].isalpha():
            raise ValueError("No existe codigo de aerolinea \
             en {}".format(numero))

        if not numero[:2].isupper():
            raise ValueError("El Codigo {} es invalido".format(numero))

        if not (numero[2:].isdigit() and int(numero[2:]) <= 9999):
            raise ValueError("Numero de ruta invalido en {}".format(numero))

        self._numero = numero
        self._aeronave = aeronave
        filas, asientos = self._aeronave.plan_asientos()
        self._asientos = [None] + [{letra: None for letra in asientos}
                                   for _ in filas]

    def numero(self):
        return self._numero

    def aerolinea(self):
        return self._numero[:2]

    def modelo_nave(self):
        return self._aeronave.modelo()

    # Como esto es un detalle se usa _
    def _parsear_asientos(self, asiento):
        filas, letras_asientos = self._aeronave.plan_asientos()

        letra = asiento[-1]
        if letra not in letras_asientos:
            raise ValueError("Letra de asiento invalida {}".format(letra))

        fila_texto = asiento[:-1]
        try:
            fila = int(fila_texto)
        except ValueError:
            raise ValueError("Fila de asiento invalida {}".format(fila_texto))

        if fila not in filas:
            raise ValueError("Numero de fila invalida {}".format(fila))

        return fila, letra

    def asignar_asiento(self, asiento, pasajero):
        fila, letra = self._parsear_asientos(asiento)

        if self._asientos[fila][letra] is not None:
            raise ValueError("El asiento {} esta ocupado".format(asiento))

        self._asientos[fila][letra] = pasajero

    def reasignar_pasajero(self, asiento_origen, asiento_destino):
        fila_origen, letra_origen = self._parsear_asientos(asiento_origen)
        if self._asientos[fila_origen][letra_origen] is None:
            raise ValueError("No hay Pasajero en el asiento \
                              {}".format(asiento_origen))

        fila_destino, letra_destino = self._parsear_asientos(asiento_destino)
        if self._asientos[fila_destino][letra_destino] is not None:
            raise ValueError("El asiento {} está ocupado"
                             .format(asiento_destino))

        self._asientos[fila_destino][letra_destino] = self._asientos[fila_origen][letra_origen]
        self._asientos[fila_origen][letra_origen] = None

    def numero_asientos_libres(self):
        return sum(sum(1 for s in filas.values() if s is None)
                   for filas in self._asientos
                   if filas is not None)

    def _asientos_pasajeros(self):
        numeros_fila, letras_asiento = self._aeronave.plan_asientos()
        for filas in  numeros_fila:
            for letras in  letras_asiento:
                pasajero = self._asientos[filas][letras]
                if pasajero is not None:
                    yield(pasajero, '{}{}'.format(filas, letras))

    def crear_tarjeta_embarque(self, impresion_tarjeta):
        for pasajero, asiento in sorted(self._asientos_pasajeros()):
            impresion_tarjeta(pasajero, asiento, self.numero(), self.modelo_nave())


class Aeronave:
    # TODO en produccion todo deberia ser validado
    def __init__(self, registro):
        self._registro = registro

    def registro(self):
        return self._registro

    def numero_asientos(self):
        filas, filas_asientos = self.plan_asientos()
        return len(filas), len(filas_asientos)


class AirbusA319(Aeronave):

    def modelo(self):
        return "Airbus A319"
    
    def plan_asientos(self):
        return range(1, 23), "ABCDEF"


class Boeing747(Aeronave):

    def modelo(self):
        return "Boeing 747"
    
    def plan_asientos(self):
        return range(1, 57), "ABCDEFGH"



def tarjeta_embarque_consola(pasajero, asiento, numero_vuelo, Aeronave):
    salida = "| Nombre {0}" \
             " Vuelo {1}" \
             " Asiento {2}" \
             " Aeronave {3}" \
             "|".format(pasajero, numero_vuelo, asiento, Aeronave)
    banner = '+' + '-' * (len(salida) - 2) + '+'
    borde = '|' + ' ' * (len(salida) - 2) + '|'
    linea = [banner, borde, salida, borde, banner]
    tarjeta = '\n'.join(linea)
    print(tarjeta)
    print()


def crear_vuelo():
    f = Vuelo("AB2455", AirbusA319("WS-123"))
    f.asignar_asiento("5A", "Antonio")
    f.asignar_asiento("10D", "Andres")
    f.asignar_asiento("12B", "Paola")
    f.asignar_asiento("8C", "Santiago")

    g = Vuelo("AG2432", Boeing747("GS-345"))
    g.asignar_asiento("1A", "Guillermo")
    g.asignar_asiento("14G", "Susana")
    g.asignar_asiento("10A", "Diana")
    g.asignar_asiento("10B", "Jhonatan")
    return f, g
