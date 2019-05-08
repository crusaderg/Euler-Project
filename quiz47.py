import time
import math

import myMathHelper

start_time = time.time()

last_Ten_Digits = 0
for n in range( 1, 1000 ):
    last_Ten_Digits += (n ** n) % (10 ** 10)

print( last_Ten_Digits % (10 ** 10)
       )

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)

