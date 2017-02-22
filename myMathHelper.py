import math

#-------------------------------------------------------
def IsPrime( val ):
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