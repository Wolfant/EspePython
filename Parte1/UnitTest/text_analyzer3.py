import unittest
import os

# Se debe escribir el codigo minimo para pasar la prueba
def analyze_text():
    pass

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

if __name__ == '__main__':
    unittest.main()

