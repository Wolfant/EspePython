# Dibujar en una pizzarra y ejecutar en REPL
c = [21, 37]
e = c * 4
[0] * 10
s = [[-1, +1 ]] * 5
s
s[3].append(7)
s

# Mas sobre listas
w = "manzana pera limon manzana durazno piña".split()
w
i = w.index('pera')
i
w[i]
w.index('unicornio')
"manzana" in w
"banana" not in w
w.count("manzana")
del w[3]
w.remove('limon')
w.insert(2,"fresa")
w
" ".join(w)
w.sort()
w
w.reverse()
w.sort(key=len)
x = [4, 9, 2, 1]
y = sorted(x)
y
p = [9, 3, 1, 0]
q = reversed(p)
q
list(q)
