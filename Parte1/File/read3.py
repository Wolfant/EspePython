#REPL
g = open("t.txt", mode = "rt", encoding='utf-8')
#sabes si aun es leible
g.readable()
# primeros 32 caracteres
g.read(32)
# leer todo el archivo
g.read()
# ya no se puede leer otra vez ya que llegue al final 
g.read()
# para regresar al inicio 
g.seek(0)
# leer de linea en linea al final muestra ''
g.readline()
g.seek(0)
# lee el archivo y crea una lista y cada objeto es una linea
g.readlines()
g.close()
