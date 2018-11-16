class Persona:
    
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    def to_string(self):
        print(self._nombre)
        print(self._apellido)
    
    


