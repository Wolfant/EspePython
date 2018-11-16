# en REPL
def gen246():
    print('generando 2')
    yield 2
    print('generando 4')
    yield 4
    print('generando 6')
    yield 3
    print('fin de generacion')

g = gen246()
next(g)
next(g)
next(g)
# error en 4
next(g)

for i in gen246():
    print(i)
