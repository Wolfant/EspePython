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
