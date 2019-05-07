import math

#-------------------------------------------------------
def IsPrime( val ):
    if (val == 1):
        return False
    if (val == 2):
        return True
    if (val % 2) == 0:
        return False

    sqrt_val = math.floor( math.sqrt(val) ) + 1
    for i in range(3, sqrt_val):
        if ( val % i ) == 0:
            return False

    return True
#-------------------------------------------------------

#-------------------------------------------------------
def GetAllDivisor(val):
    lst_Divisor = []
    for divisor in range(1, int((val/2)) + 1):
        if (val % divisor) == 0:
            lst_Divisor.append(divisor)

    return lst_Divisor
#-------------------------------------------------------

#-------------------------------------------------------
def GetFibNumber(pos):
    fib1 = 1
    fib2 = 1
    fib  = 0
    for i in range(3, pos + 1):
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib    

    return fib
#-------------------------------------------------------

#-------------------------------------------------------
def ConvertListToInt(digit_list):
    number = 0
    for i in digit_list:                                            
        number = number * 10 + i

    return number 
#-------------------------------------------------------

#-------------------------------------------------------
def GetPandigital(digit_width):
    panDigits  = []
    digit_list = []
    for num1 in range( 1, 10 ):        
        if not num1 in digit_list:
            digit_list.append( num1 )            
        else:
            continue
        
        if digit_width == 1:
            panDigits.append( ConvertListToInt(digit_list) )
           
        for num2 in range( 0, 10 ):
            if not num2 in digit_list:                
                digit_list.append( num2 )
            else:
                continue 

            if digit_width == 2:
                panDigits.append( ConvertListToInt(digit_list) )

            for num3 in range( 0, 10 ):
                if not num3 in digit_list:
                    digit_list.append( num3 ) 
                else:
                    continue

                if digit_width == 3:
                    panDigits.append( ConvertListToInt(digit_list) )

                for num4 in range( 0, 10 ):
                    if not num4 in digit_list:
                        digit_list.append( num4 ) 
                    else:
                        continue

                    if digit_width == 4:
                        panDigits.append( ConvertListToInt(digit_list) )

                    for num5 in range( 0, 10 ):
                        if not num5 in digit_list:
                            digit_list.append( num5 ) 
                        else:
                            continue

                        if digit_width == 5:
                            panDigits.append( ConvertListToInt(digit_list) )

                        for num6 in range( 0, 10 ):
                            if not num6 in digit_list:
                                digit_list.append( num6 ) 
                            else:
                                continue

                            if digit_width == 6:
                                panDigits.append( ConvertListToInt(digit_list) )

                            for num7 in range( 0, 10 ):
                                if not num7 in digit_list:
                                    digit_list.append( num7 ) 
                                else:
                                    continue

                                if digit_width == 7:
                                    panDigits.append( ConvertListToInt(digit_list) )

                                for num8 in range( 0, 10 ):                                                               
                                    if not num8 in digit_list:
                                        digit_list.append( num8 ) 
                                    else:
                                        continue

                                    if digit_width == 8:
                                        panDigits.append( ConvertListToInt(digit_list) )

                                    for num9 in range( 0, 10 ):                                  
                                        if not num9 in digit_list:
                                            digit_list.append( num9 ) 
                                        else:
                                            continue

                                        if digit_width == 9:
                                            panDigits.append( ConvertListToInt(digit_list) )

                                        for num10 in range( 0, 10 ):
                                            if not num10 in digit_list:
                                                digit_list.append( num10 ) 
                                            else:
                                                continue

                                            if digit_width == 10:
                                                panDigits.append( ConvertListToInt(digit_list) )

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

    return panDigits
#-------------------------------------------------------