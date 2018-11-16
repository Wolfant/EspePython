# Dibujar en una pizzarra y ejecutar en REPL
a = [[1, 2, 3], [4, 5, 6]]
b = a[:]
a is b
a == b
# el objeto es distinto pero los inner object son los mismos
a[0] is b[0]
a[1] is b[1]
# si se modifica el inner object se modifica el objeto inicial
a[0] = [8, 9]
# por lo tanto se crea un nuevo inner object que pertenece al objeto inicial
a
b
a[0] is b[0]
a[0] == b[0]
# si se aumenta un abjeto a un inner object
a[1].append(7)
# las referencias no se modifican por lo tanto siguen siendo el mismo inner object
a[1] is b[1]
a
b
