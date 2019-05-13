import time

import myMathHelper

start_time = time.time()


MAX_PRIME_NUDER_1MILLION = 999999
PRIME_LIST_NUDER_1MILLION = [ 2 ]
for n in range( 3, MAX_PRIME_NUDER_1MILLION + 1, 2 ):
    if myMathHelper.IsPrime( n ):
        PRIME_LIST_NUDER_1MILLION.append( n )

print( 'Total %d primes under %d' % ( len( PRIME_LIST_NUDER_1MILLION ), MAX_PRIME_NUDER_1MILLION + 1) )

longest_ConsecutivePrime_PrimeTermNumber = 0
longest_ConsecutivePrime = 0
longest_ConsecutivePrime_PrimeTerms = []
for index in range( len( PRIME_LIST_NUDER_1MILLION ) - 1, 0, -2 ):
    prime = PRIME_LIST_NUDER_1MILLION[ index ]
    start_Index = 0
    end_Index   = len( PRIME_LIST_NUDER_1MILLION ) // 2
    while True:
        sum_Prime = sum( PRIME_LIST_NUDER_1MILLION[ start_Index : end_Index ] )
        if sum_Prime < prime:
            break
        end_Index = end_Index // 2
        if end_Index == 0:
            break
    sum_Prime = sum( PRIME_LIST_NUDER_1MILLION[ start_Index : end_Index ] )
    while True:
        if sum_Prime < prime:
            end_Index += 1
            sum_Prime += PRIME_LIST_NUDER_1MILLION[ end_Index ]
        else:
            break
    sum_Prime = sum( PRIME_LIST_NUDER_1MILLION[ start_Index : end_Index ] )
    while True:
        if sum_Prime == prime:
            if longest_ConsecutivePrime_PrimeTermNumber < end_Index - start_Index:
                longest_ConsecutivePrime_PrimeTermNumber = end_Index - start_Index
                longest_ConsecutivePrime = prime
                longest_ConsecutivePrime_PrimeTerms = list( PRIME_LIST_NUDER_1MILLION[ start_Index : end_Index ] )
        elif sum_Prime < prime:
            break
        sum_Prime -= PRIME_LIST_NUDER_1MILLION[ start_Index ]
        start_Index += 1

print( '' )
print( 'Longest consecutive prime %d has %d terms: ' % ( longest_ConsecutivePrime, longest_ConsecutivePrime_PrimeTermNumber ), end = '' )
print( longest_ConsecutivePrime_PrimeTerms )

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)
