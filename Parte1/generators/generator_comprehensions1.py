#EN REPEL
million_squares = (x*x for x in range(1,1000001))
million_squares
# Pimera vez hay datos
list(million_squares)
# Ya no existen los datos
list(million_squares)
sum(x*x for x in range(1,1000001))

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False    
    return True

sum(x for x in range(1,1000001) if is_prime(x))