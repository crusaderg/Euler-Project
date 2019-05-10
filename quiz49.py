import time
import math

import myMathHelper

start_time = time.time()

NUMBER_WIDTH = 12
MIN_NUMBER = 1000
MAX_NUMBER = 9999
for number in range( MIN_NUMBER, MAX_NUMBER ):
    if myMathHelper.IsPrime( number ):
        if myMathHelper.IsPrime( number + 3330 ) and myMathHelper.IsPrime( number + 3330 * 2 ):
            list_Number1 = []
            list_Number2 = []
            list_Number3 = []
            number1 = number
            number2 = number + 3330
            number3 = number + 3330 * 2
            for i in range( 1, NUMBER_WIDTH + 1 ):
                list_Number1.append( number1 % 10 )
                list_Number2.append( number2 % 10 )
                list_Number3.append( number3 % 10 )
                number1 = number1 // 10
                number2 = number2 // 10
                number3 = number3 // 10
            list_Number1.sort()
            list_Number2.sort()
            list_Number3.sort()
            if list_Number1 == list_Number2 and list_Number1 == list_Number3:
                print( '%d %d %d' % ( number, number + 3330, number + 3330 * 2 ) )

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)
