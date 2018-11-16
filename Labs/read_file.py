#!/usr/bin/python3
"""
read_file.py
Obtiene e imprime las palabras de un archivo en UTF-8

Usage:
    python3 read_file.py <file>

License:
    GnuGPL v3.0
"""

import sys

__author__ = "Antonio Insuasti"
__version__ = 1.2
__credits__ = ["Edison", "Mauricio"]
__maintainer__ = "Juan"
__email__ = "antonio@insuasti.ec"

def extraer_palabras(file):
    """Obtiene la lista de palabras de un archivo de text


    Args:
        file: Archivo de texto en UTF-8

    Returns:
        Una lista de str con todas las palabras del documento
    """
    with open(file, 'rt') as historia:
        palabras_historia = []
        for linea in historia:
            linea_historia = linea.split()
            for palabra in linea_historia:
                palabras_historia.append(palabra)
    return palabras_historia


def imprimir_iterable(items):
    """ Imprime objetos de un iterable

    Args:
        items: Lista de objetos a imprimir

    Returns:
        None
    """
    for item in items:
        print(item)


def main(file):
    """ Imprime las palabras de un archivo UTF-8
    Args:
        file: Archivo UTF-8
    """
    items = extraer_palabras(file)
    imprimir_iterable(items)


if __name__ == '__main__':
    main(sys.argv[1])
