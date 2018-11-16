#Ejecutar en REPL
s = "show how to index into squences".split()
s
full_slice = s[:]
full_slice is s
full_slice == s
# usando la funcion copy
u = s.copy
# usando el constructor
v = list(s)


