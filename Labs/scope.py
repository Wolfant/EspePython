count = 0

def show_count():
    print('count = ', count)

def set_count(c):
    global count
    count = c

def id_count():
    global count
    return id(count)

def modify(k = []):
    k.append(39)
    print("K => ", k)

def fun(**kwargs):
    print(type(kwargs))
    _dic2_local = kwargs
    for key, value in _dic2_local.items():
        print("{0} => {1}".format(key,value))



def imprime_algo(num):
    print("esto es la funcion principal")
    def print_one():
        print("One")
    def print_two():
        print("two")
    if num == 1:
        return print_one
    else:
        return print_two
