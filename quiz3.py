import math
import time

NUMBER = 600851475143
MAX_PRIMEFACTOR = 1

#-------------------------------------------------
def IsPrime( val ):
    if (val % 2) == 0:
        return False

    sqrt_val = math.floor( math.sqrt(val) ) + 1
    for i in range(3, sqrt_val):
        if ( val % i ) == 0:
            return False

    return True
#-------------------------------------------------

val_NUMBER = NUMBER
factor     = 0
t_start    = time.time()
for factor in range(2, int(val_NUMBER / 2) + 1):
	if (val_NUMBER % factor) == 0:
		val_NUMBER = val_NUMBER / factor
		if (val_NUMBER == 1):
			break
		if (IsPrime(factor) == False):
			continue		
		if (factor > MAX_PRIMEFACTOR):
			MAX_PRIMEFACTOR = factor

if (NUMBER % factor) == 0 and (IsPrime(factor) == True) and (factor > MAX_PRIMEFACTOR):
	MAX_PRIMEFACTOR = factor

print('Used %d seconds: ' % (time.time() - t_start))
print('Max prime factor：%d' % MAX_PRIMEFACTOR)

