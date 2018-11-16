import sys

def gen246():
    ''' Funcion ejemplo generador '''
    yield 2
    yield 4
    yield 6

def toma_dato(count, var_iterable):
    ''' toma un item del iterable
    Args:
        count: numero maximo de  items a retornar
        var_iterable: serie de datos
    
    Yields:
        Al menos 'count' items del 'var_iterable' 
    '''
    counter = 0
    for item in var_iterable:
        if count == counter:
            return
        counter += 1
        yield item     

def distinct(iterable):
    seen = set()
    # Convierto en set para eliminar repetidos
    try:
        for item in iterable:
            if item in seen:
                continue
            seen.add(item)
            yield item
    except TypeError:
        raise  

def ejecuta_toma_dato():
    items = ["persona" , "persona", 1, [1 ,2 , 4] , 8, 'persona', 10]
    try:
        x = toma_dato(3, distinct(items))
        for item in x:
            print(item)
    except TypeError as e: 
        print(e)
    finally:
        print("Final")

    


if __name__ == '__main__':
    ejecuta_toma_dato()
