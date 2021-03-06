import unittest
import os

# Se debe escribir el codigo minimo para pasar la prueba
# Se agrega el filename para que pase la prueba
def analyze_text(filename):
    """Calcula el numero de lineas en un archivo
    
    Args:
        filename: El nombre del archivo
    
    Raises: IOError: Error si no encuentra  leer o encontrar el archivo.
    
    Returns: El numero de lineas en el archivo.
    """
    with open(filename, 'rt') as line:
        return sum(1 for _ in line)


class TextAnalysisTests(unittest.TestCase):
    """Test para la funcion ``analyze_text()`` """
    
    #fixture que corre antes de las pruebas
    def setUp(self):
        """Fixture para crear el archivo para uso en metodos"""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'wt') as f:
            f.write(" Esto es un texto de prueba.\n"
                    "Deberia tener mas de una linea\n"
                    "para que sea util en la prueba \n")

    #fixture que corre despues de las pruebas
    def tearDown(self):
        """Fixture que elimina el archivo creado"""
        try:
            os.remove(self.filename)
        except:
            pass

    # Toda funcion que inicia con test_ se ejecuta
    # falla porque analyze_text aun no recibe un parametro
    def test_funciont_runs(self):
        """Basic smoke test: ejecuta la funcion. """
        analyze_text(self.filename)

    #Prueba que exista 3 lineas en el archivo
    # Se modifica para obtener una tupla
    def test_line_count(self):
        """Prueba que la cuenta de lineas sea correcta"""
        self.assertEqual(analyze_text(self.filename)[0], 3)
    
    #Prueba que exitan 95 caracteres
    def test_characters_count(self):
        """Prueba que la cuenta de caracteres sea correcta"""
        self.assertEqual(analyze_text(self.filename)[1], 92)

if __name__ == '__main__':
    unittest.main()
