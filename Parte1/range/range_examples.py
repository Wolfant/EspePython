# 1 No abusar de range
# Python no es C
# No se debe ser un-Pythonic
s = [0, 1, 4, 6, 13]
for i in range(len(s)):
    print(s[i])

# se prefiere iteraciones directas sobre objectos
# como listas
for v in s:
    print(v)

# No usar range para enumerar,
# para eso hay enumerate()
# esta funcion mejora el 
# rendimiento en tuplas (index, value)
t = [6, 372, 8862, 14880, 2096886]
for p in enumerate(t):
    print(p)
# con frecuencia se usa con unpack de tuplas

for i, v in enumerate(t):
    print("i = {}, v = {}".format(i,v))



