def take(count, iterable):
    '''Toma un item del iterable

    Args:
        count: El numero maximo de items por devolver
        iterable: La serie de datos

    Yields:
        Al menos 'count' items del 'iterable'
    '''
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def distinct(iterable):
    '''Retorna items unicos eliminado los duplicados

    Args:
        iterable: La serie de datos

    Yields:
        elementos unicos en orden del 'iterable'
    '''
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_pipeline():
    items = [3, 6, 6, 2 , 1 ,1]
    for item in take(3, distinct(items)):
        print(item)


if __name__ == '__main__':
    run_pipeline()
