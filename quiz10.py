from math import floor, sqrt
import time

#-------------------------------------------------
def IsPrime( val ):
    if (val % 2) == 0:
        return False

    sqrt_val = floor( sqrt(val) ) + 1
    for i in range(3, sqrt_val):
        if ( val % i ) == 0:
            return False

    return True
#-------------------------------------------------

MAX_NUMBER = 2000000
sum = 2

tm_Start = time.time()
for i in range(2, MAX_NUMBER + 1):
    if IsPrime(i) == True:
        sum += i
tm_End   = time.time()

print('Sum under %d is %d' % (MAX_NUMBER, sum))
print('Elapsed %d seconds' % (tm_End - tm_Start))