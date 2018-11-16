"""Obtiene e imprime las parabras de un archivo de texto UTF-8

Usage:

    python3 modulo_doc.py <file>

"""
import sys


def fetch_words(file):
    """ Obtine la lista de palabras de un archivo
    Args:
        file: Archivo de texto en UTF-8
    
    Returns:
        Una lista  de strings con todas las palabras del documento
    """
    with open(file, 'r') as story:
        story_words = []
        for line in story:
            line_words = line.split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    """ Imprime la lista de items en una lista

    Args:
        items: lista de objetos a imprimir
    """
    for item in items:
        print(item)


def main(file):
    """Imprime las palabras de un archivo

    Args:
       file: Archivo de texto en UTF-8 
    """
    words = fetch_words(file)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])
