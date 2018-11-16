# Ejecutar en REPL
# Funcion que toma un diccionario de tamaño variable
def fun(**kwargs): 
    # kwargs es un diccionario 
    print(type(kwargs)) 
    # imprimo los items
    for key in kwargs: 
        print("%s = %s" % (key, kwargs[key])) 
  
# Driver code 
fun(name="Python", ID="101", language="class") 
