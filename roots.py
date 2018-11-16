def sqrt(x):
    '''Compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed.
    
    Returns:
        The square root of x
    
    Raises: 
        ValueError: en caso que se envie un dato negativo
    '''
    if x <= 0:
         raise ValueError(" No existe raiz cuadrada de "
          "nuemero negativos")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess

def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print(sqrt(0))
        print(sqrt('hola'))
    except ValueError as e:
        print("Error en la ejecucion del programa {}".format(e))
    finally:
        print("fin en la ejecucion del programa")


if __name__ == "__main__":
    main()