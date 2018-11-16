import unittest
import os

# Se debe escribir el codigo minimo para pasar la prueba
# Se agrega el filename para que pase la prueba
# Se programa para que pase la prueba
def analyze_text(filename):
    """Calcula el numero de lineas en un archivo
    
    Args:
        filename: El nombre del archivo
    
    Raises: IOError: Error si no encuentra  leer o encontrar el archivo.
    
    Returns: Tupla el primer item es el numero de lineas
        el segundo item es el numero de caracteres
    """
    lines = 0
    characters = 0
    with open(filename, 'rt') as f:
        for line in f:
            lines += 1
            characters += len(line)  
    return (lines, characters)


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
    
    # Prueba si el archivo no existe
    def test_no_such_file(self):
        """Prueba que lanze un error IOError en caso que no encuentre el archivo"""
        with self.assertRaises(IOError):
            analyze_text("root.txt")


if __name__ == '__main__':
    unittest.main()
