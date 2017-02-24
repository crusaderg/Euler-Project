import math

#-------------------------------------------------------
def IsPrime( val ):
    if (val % 2) == 0:
        return False

    sqrt_val = math.floor( math.sqrt(val) ) + 1
    for i in range(3, sqrt_val):
        if ( val % i ) == 0:
            return False

    return True
#-------------------------------------------------------

primes = (x for x in range(1000, 7, -1) if IsPrime(x))

for i in primes:
    F = (map(lambda x: 10**x, range(2, i)))
    for j in F:
        if (j-1)%i == 0:
            break
    if len(str(j)) == i:
        print(i)
        break