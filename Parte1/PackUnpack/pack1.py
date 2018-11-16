# Ejecutar en REPL
def mySum(*args): 
    sum = 0
    for i in range(0, len(args)): 
        sum = sum + args[i] 
    return sum 
  
# Driver code 
print(mySum(1, 2, 3, 4, 5)) 
print(mySum(10, 20))
 
