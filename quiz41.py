import sys
import time

import myMathHelper  

def Is_Pandigital_Prime( digit_list ):
    number = 0
    for i in digit_list:                                            
        number = number * 10 + i                                        
    if myMathHelper.IsPrime( number ):
        return number

    return 0
#-------------------------------------------------------

start_time = time.time()

result = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0 }
digit_list = []
for num1 in range( 9, 1, -1 ):
    digit_list.append( num1 )
    number = Is_Pandigital_Prime( digit_list )
    if number > 0:
        if max(digit_list) <= 1 and result[1] < number:
            result[1] = number
    for num2 in range( 9, 0, -1 ):
        if num2 in digit_list:
            continue
        else:
            digit_list.append( num2 )
            number = Is_Pandigital_Prime( digit_list )
            if number > 0:
                if max(digit_list) <= 2 and result[2] < number:
                    result[2] = number
        for num3 in range( 9, 0, -1 ):
            if num3 in digit_list:
                continue
            else:
                digit_list.append( num3 )
                number = Is_Pandigital_Prime( digit_list )
                if number > 0:
                    if max(digit_list) <= 3 and result[3] < number:
                        result[3] = number
            for num4 in range( 9, 0, -1 ):
                if num4 in digit_list:
                    continue
                else:
                    digit_list.append( num4 )
                    number = Is_Pandigital_Prime( digit_list )
                    if number > 0:
                        if max(digit_list) <= 4 and result[4] < number:
                            result[4] = number
                for num5 in range( 9, 0, -1 ):
                    if num5 in digit_list:
                        continue
                    else:
                        digit_list.append( num5 )
                        number = Is_Pandigital_Prime( digit_list )
                        if number > 0:
                            if max(digit_list) <= 5 and result[5] < number:
                                result[5] = number
                    for num6 in range( 9, 0, -1 ):
                        if num6 in digit_list:
                            continue
                        else:
                            digit_list.append( num6 )
                            number = Is_Pandigital_Prime( digit_list )
                            if number > 0:
                                if max(digit_list) <= 6 and result[6] < number:
                                    result[6] = number
                        for num7 in range( 9, 0, -1 ):
                            if num7 in digit_list:
                                continue
                            else:
                                digit_list.append( num7 )
                                number = Is_Pandigital_Prime( digit_list )
                                if max(digit_list) <= 7 and number > 0:
                                    if result[7] < number:
                                        result[7] = number
                            for num8 in range( 9, 0, -1 ):                                                               
                                if num8 in digit_list:
                                    continue
                                else:
                                    digit_list.append( num8 )
                                    number = Is_Pandigital_Prime( digit_list )
                                    if number > 0:
                                        if max(digit_list) <= 8 and result[8] < number:
                                            result[8] = number
                                for num9 in range( 9, 0, -1 ):                                  
                                    if num9 in digit_list:
                                        continue
                                    else:
                                        digit_list.append( num9 )
                                        number = Is_Pandigital_Prime( digit_list )
                                        if number > 0:
                                            if max(digit_list) <= 9 and result[9] < number:
                                                result[9] = number
                                    for num10 in range( 9, 0, -1 ):
                                        if num10 in digit_list:
                                            continue
                                        digit_list.append( num10 )
                                        number = Is_Pandigital_Prime( digit_list )
                                        if number > 0:
                                            if max(digit_list) <= 10 and result[10] < number:
                                                result[10] = number            
                                        del digit_list[-1]
                                    del digit_list[-1]
                                del digit_list[-1]
                            del digit_list[-1]
                        del digit_list[-1]
                    del digit_list[-1]       
                del digit_list[-1]
            del digit_list[-1]
        del digit_list[-1]

    digit_list.clear()

print( result )

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)