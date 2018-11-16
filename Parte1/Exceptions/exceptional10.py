'''Modulo para demostrar errores'''

import sys
from math import log

def convert(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion Error: {}"\
                .format(str(e), file = sys.stderr))
        return -1


def string_log(s):
        v = convert(s)
        return log(v)
