def fun_infinita():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a , b = b , a + b
