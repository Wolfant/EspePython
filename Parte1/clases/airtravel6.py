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

    def asignar_asiento(self, asiento, pasajero):
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

        if self._asientos[fila][letra] is not None:
            raise ValueError("El asiento {} esta ocupado".format(asiento))

        self._asientos[fila][letra] = pasajero


class Aeronave:
    # TODO en produccion todo deberia ser validado
    def __init__(self, registro, modelo,
                 numero_filas, numero_asientos_por_fila):
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
