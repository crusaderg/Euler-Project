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