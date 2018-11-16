import unittest


class TextAnalysisTests(unittest.TestCase):
    """Test para la funcion ``analyze_text()`` """
    # Toda funcion que inicia con test_ se ejecuta
    def test_funciont_runs(self):
        """Basic smoke test: ejecuta la funcion. """
        analyze_text()

if __name__ == '__main__':
    unittest.main()

