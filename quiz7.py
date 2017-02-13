import math

#------------------------------------------------
def IsPrime( val ):
    if (val % 2) == 0:
        return False

    sqrt_val = math.floor( math.sqrt(val) ) + 1
    for i in range(3, sqrt_val):
        if ( val % i ) == 0:
            return False

    return True
#-------------------------------------------------

th_PRIME  = 10001
count     = 0
val_Prime = 1
val       = 1

#-------------------------------------------------
while (count < th_PRIME):
    if (IsPrime(val) == True):
        count = count + 1
        val_Prime = val    

    val = val + 1
#-------------------------------------------------
    
print('The %dth prime is %d' % (th_PRIME, val_Prime));