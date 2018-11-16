""" Modelo para vuelo de aviones"""


class Vuelo:

    def __init__(self, numero):
        if not numero[:2].isalpha():
            raise ValueError("No existe codigo de aerolinea \
             en {}".format(numero))

        if not numero[:2].isupper():
            raise ValueError("El Codigo {} es invalido".format(numero))

        if not (numero[2:].isdigit() and int(numero[2:]) <= 9999):
            raise ValueError("Numero de ruta invalido en {}".format(numero))

        self._numero = numero

    def numero(self):
        return self._numero

    def aerolinea(self):
        return self._numero[:2]
