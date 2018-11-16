import unittest
import os

def analisis_texto(filename):
    with open(filename,mode = 'rt') as f:
        lineas = 0
        caracteres = 0
        for linea in f:
            lineas += 1
            caracteres += len(linea)

    return lineas , caracteres

class AnalisisTextoTest(unittest.TestCase):
    """Test para la funcion ``analisis_texto()``"""
    
    def setUp(self):
        '''Fixture para crear el archivo que vamos a usar'''
        self.filename = 'text_analizy_file.txt'
        with open(self.filename, 'wt') as f:
            f.write('Esto es el arhivo de prueba.\n'
                     'Esta es la segunda linea \n'
                     'Esta es la tercera linea \n')

    def tearDown(self):
        '''Fixture para borrar el archivo usado en las pruebas'''
        try:
            os.remove(self.filename)
        except:
            pass
    
    # toda funcion que inicia con test_ se ejecuta
    def test_funcion_runs(self):
        '''Prueba basica: La ejecucion se ejeucta? '''
        analisis_texto(self.filename)
    
    def test_cuenta_linea(self):
        '''Prueba que se cuente las lineas y retorne dato '''
        ''' tambien prueba que exista un return '''
        self.assertEqual(analisis_texto(self.filename)[0], 3)
    
    def test_funcion_retorno(self):
        '''prueba que la funcion retorno dos datos'''
        self.assertEqual(len(analisis_texto(self.filename)), 2)

    def test_cuenta_caracteres(self):
        ''' Prueba basica para contar caracteres'''
        self.assertEqual(analisis_texto(self.filename)[1], 81)

    
    

if __name__ == '__main__':
    unittest.main()