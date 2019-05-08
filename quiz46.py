import time
import math

import myMathHelper

start_time = time.time()

Goldbach_Is_Wrong = False
First10000PrimeList = myMathHelper.GetFirst10000Prime()
for odd_Composite_Number in range( 9, 22, 2 ):
    if myMathHelper.IsPrime( odd_Composite_Number ):
        continue
    
    prime_Index = 0
    Goldbach_Is_Wrong = True
    while First10000PrimeList[prime_Index] < odd_Composite_Number:        
        number = odd_Composite_Number - First10000PrimeList[prime_Index]
        prime_Index += 1
        if number % 2 != 0:
            continue
        number = number / 2
        #print( number )
        if math.sqrt( number ) == math.floor( math.sqrt( number ) ):
            Goldbach_Is_Wrong = False
            break

    if Goldbach_Is_Wrong:
        print( odd_Composite_Number )
        break

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)

'''
What are odd composite numbers?

An odd number is an integer that is not evenly divisible by 2.

A composite number is a positive number that has divisors other than 1 and itself.

So any odd number greater than 1 that is not prime would be a composite odd number.

For example, 9, 15, 21, and 25 are odd composite number because the are odd and they have divisors.

1, 3, 5, and 7 are not composite because they are only divisible by 1 and themselves.
'''