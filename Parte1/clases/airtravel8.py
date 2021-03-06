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


class Aeronave:
    # TODO en produccion todo deberia ser validado
    def __init__(self, registro, modelo,
                 numero_filas,
                 numero_asientos_por_fila):
        self._registro = registro
        self._modelo = modelo
        self._numero_filas = numero_filas
        self._numero_asientos_por_fila = numero_asientos_por_fila

    def registro(self):
        return self._registro

    def modelo(self):
        return self._modelo

    def plan_asientos(self):
        return (range(1, self._numero_filas + 1),
                "ABCDEFGHJ"[:self._numero_asientos_por_fila])


def crear_vuelo():
    f = Vuelo("AB2455", Aeronave(234, "Boing 747", 13, 6))
    f.asignar_asiento("5A", "Antonio")
    f.asignar_asiento("10D", "Andres")
    f.asignar_asiento("12B", "Paola")
    f.asignar_asiento("8C", "Santiago")
    return f
