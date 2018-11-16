'''Modulo para demostrar errores'''

import sys

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion Error: {}"\
                .format(str(e), file = sys.stderr))
        return -1