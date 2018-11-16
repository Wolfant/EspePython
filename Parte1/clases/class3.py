class MyClass:
    """Una clase simple para ejemplo"""

    def __init__(self, number):
        self._number = number

    def number(self):
        """ Funcion que retorna el valor de atributo de clase MyClass

            Return:
                object: el valor de "number"
        """
        return self._number

    def imprime(self):
        """ Funcion que imprime el hola mundo con el valor de "number"

            Return:
                str: hola mundo con el valor de "number"
        """
        print("Hola Mundo mi atributo number es {}".format(self._number))
