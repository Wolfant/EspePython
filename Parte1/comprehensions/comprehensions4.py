
from pprint import pprint as pp

pais_capital = { "Ecuad0r": "Quito",
                "Peru": "Lima",
                "Colombia": "Bogota",
                "Brasil": "Brasilia" }

capital_pais = { capital: pais for pais, capital in pais_capital.items() }
pp(capital_pais)


