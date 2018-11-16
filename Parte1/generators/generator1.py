# en REPL
def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
next(g)
next(g)
next(g)
# error en 4
next(g)

for i in gen123():
    print(i)

h = gen123()
i = gen123()
h
i
h is i
next(h)
next(h)
next(i)
