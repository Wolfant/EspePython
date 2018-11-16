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


def run_take():
    items = [2, 4, 6, 8 , 10]
    for item in take(2, items):
        print(item)


if __name__ == '__main__':
    run_take()
