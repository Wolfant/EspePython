#REPL
f = open("t.txt", mode = "wt", encoding='utf-8')
help(f)
f.write("Esta es una nueva liea ")
f.write("esta siguie siendo la misma linea \n")
# no existe writeline
f.write("Otra super linea \n")
# cerrar el archivo
f.close()
