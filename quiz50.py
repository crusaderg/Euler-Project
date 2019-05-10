import time
import myMathHelper

start_time = time.time()

MAX_PRIME_NUDER_1MILLION = 999983
counter = 0
for n in range( 10, 1, -2 ):
    print( n )
    counter += 1
    #if myMathHelper.IsPrime( n ):
    #    counter += 1

print( counter )

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)
