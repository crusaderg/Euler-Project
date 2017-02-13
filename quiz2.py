MAX_FIB_LIMIT = 4000000
fib1 = 1
fib2 = 2
sum  = 2

while fib1 < MAX_FIB_LIMIT:
    fib1 , fib2 = fib2 , fib1 + fib2
    if ( fib2 % 2 ) == 0: 
        sum = sum + fib2   
    
print("%d " % sum)