def transformar_int(x):
    """Funcion que trasforma un objeto a int 
    Args:
        x: objeto a transformar
    
    Returns:
        Valor del objeto en int
    
    Raises:
       ValueError: En caso de que sea str
       TypeError: en caso de que sea un objeto contenedor
    """
    
    try:
        return (int(x))
    except (ValueError, TypeError) as e:
        raise e

def main():
    numero = input('Ingrese un numero: ')
    print(transformar_int(numero))

def test_funcion():
    entero = 34
    cadena = '56'
    lista = [1, 2, 34]
    palabra = "hola"
    try: 
        print(transformar_int(entero))
        print(transformar_int(cadena))
        print(transformar_int(lista))
        print(transformar_int(palabra))
        print ('esto nunca va a mostrarse')
    except (ValueError, TypeError):
        print('error')
    print ('esto siempre se ejecuta')
    

if __name__ == '__main__':
    test_funcion()