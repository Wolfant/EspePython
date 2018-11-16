# abro el archivo
g = open("t.txt", mode = "at", encoding='utf-8')
# grego data
g.writelines('hola')
g.writelines('chao')
# este si es el final de la linea
g.writelines("aqui termina la linea\n")
g.close()
