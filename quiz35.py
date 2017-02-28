import math
from datetime import datetime

def IsPrime( val ):
    if (val == 2):
        return True
    if (val % 2) == 0:
        return False
    
    sqrt_val = math.floor( math.sqrt(val) ) + 1
    for i in range(3, sqrt_val):
        if ( val % i ) == 0:
            return False

    return True
#-------------------------------------------------------

def IsCircularPrime(val):
    if val < 10:
        return True
    strVal = str(val)
    for i in range(1, len(strVal)):
        step1 = 10 ** (len(strVal) - i)
        step2 = 10 ** i
        num  = ((val % step1) * step2) + math.floor(val / step1)
        if (IsPrime(num) == False):
            return False

    return True
#-------------------------------------------------------

count_CircularPrime  = 0
lst_CircularPrimes   = []
tm_Start   = datetime.now()
for i in range(2, 1000001):
    if IsPrime(i) == False:
        continue
    if IsCircularPrime(i) == True:
        count_CircularPrime += 1
        lst_CircularPrimes.append(i)

print(lst_CircularPrimes)
print(count_CircularPrime)
print('Finished under 1 million..., used ', end='')
print(datetime.now() - tm_Start)


