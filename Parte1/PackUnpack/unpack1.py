# Ejecutar en REPL

def fun(a, b, c, d): 
    print(a, b, c, d) 
  
# Driver Code 
my_list = [1, 2, 3, 4] 
  
# Unpacking list en 4 argumentos 
fun(*my_list) 

# Ejemplo con rang
range(3, 6)  # normal call with separate arguments 
[3, 4, 5] 
args = [3, 6] 

range(*args)  # arguments unpacked from a list 
[3, 4, 5] 


