def modify(k):
    k.append(39)
    print("K => ", k)

def replace_int(x):
    # este valor solo exite en este scope
    x = 20
    print("nuevo valor ",x)

def replace_content(g):
    # g debe tener mas de 2 items
    g[0] = 17
    g[1] = 29
    g[2] = 31
    print("g = ",g)

def normalizar_nombre(nombre , apellido):
    return nombre + ' ' + apellido

def sumar(a, c,  b = 1 ):
# siempre sumo 1    
    return a + b + c

def banner(message, border = '-'):
    print(border * len(message))
    print(message)
    print(border * len(message))




