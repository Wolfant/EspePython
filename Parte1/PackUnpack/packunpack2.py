# funcion que imprime exactamente 3 argumentos
def fun1(a, b, c): 
    print(a, b, c) 
 
# PACKING. 
# se crea un tupla *args.
# debe tener mas de dos argumentos 
# los dos deben ser str 
def fun2(*args): 
    # Convierte la tupa en lista.. porque? 
    args = list(args) 
    # Modifico los argumentos 
    args[0] = 'Python'
    args[1] = 'Rocks'
    # UNPACKING de args y ejecuto fun1() 
    fun1(*args) 
  
# Ejecucion
fun2('Hello', 'beautiful', 'world!') 
