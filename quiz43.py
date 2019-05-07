import time 
import myMathHelper

start_time = time.time()

pan_Digits = myMathHelper.GetPandigital( 10 )

sum = 0
divisors = [ 2, 3, 5, 7, 11, 13, 17 ]
for pan_Digit in pan_Digits:
    start_Index = 2
    found = True

    for divisor in divisors:
        number = pan_Digit // ( 10 ** ( 10 - start_Index + 1 - 3 ) )
        number = number % 1000
        if number % divisor != 0:
            found = False
            break
        start_Index += 1

    if found:
        sum += pan_Digit
        
print( 'Sum = %d' % sum )        

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)