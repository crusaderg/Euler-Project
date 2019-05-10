import time
import myMathHelper

'''
134043: [3, 7, 13, 491]
134044: [31, 47, 23, 4]
134045: [5, 17, 19, 83]
134046: [11, 3, 677, 2]
'''

start_time = time.time()

MAX_N_DIGIT = 4
factor_List = []
res1 = 0
res2 = 0
res3 = 0
res4 = 0
TotalRes = {}
number = 100000
is_Found = False
while not is_Found:
    number += 1
    print( number )

    factor_List = myMathHelper.GetAllPrimeDivisor( number )
    if not 2 in factor_List and len( factor_List ) != MAX_N_DIGIT:
        continue

    n = 0
    for factor in factor_List:
        if factor == 2:
            n += 1
    if n > 0:
        factor_List = list( set( factor_List ) )
        factor_List.remove( 2 )
        factor_List.append( 2 ** n )

    if len( factor_List ) != len( set( factor_List ) ):
        continue

    if len( factor_List ) != MAX_N_DIGIT:
        continue

    TotalRes[number] = list( factor_List )
    if res1 == 0:
        res1 = number
    elif res2 == 0:
        if number - res1 == 1:
            res2 = number
        else:
            res1 = number
    elif res3 == 0:
        if number - res2 == 1:
            res3 = number
            if MAX_N_DIGIT == 3:
                is_Found = True
        else:
            res1 = number
            res2 = 0
    elif res4 == 0:
        if number - res3 == 1:
            res4 = number
            is_Found = True
        else:
            res1 = number
            res2 = 0
            res3 = 0

if MAX_N_DIGIT == 4 and res1 in TotalRes and res2 in TotalRes and res3 in TotalRes and res4 in TotalRes:
    print( '%d' % res1, end = ': ' )
    print( TotalRes[res1] )
    print( '%d' % res2, end = ': ' )
    print( TotalRes[res2] )
    print( '%d' % res3, end = ': ' )
    print( TotalRes[res3] )
    print( '%d' % res4, end = ': ' )
    print( TotalRes[res4] )
elif MAX_N_DIGIT == 3 and res1 in TotalRes and res2 in TotalRes and res3 in TotalRes:
    print( '%d' % res1, end = ': ' )
    print( TotalRes[res1] )
    print( '%d' % res2, end = ': ' )
    print( TotalRes[res2] )
    print( '%d' % res3, end = ': ' )
    print( TotalRes[res3] )
else:
    print( 'Not found!!!' )
    #print( TotalRes )

'''
MAX_N_DIGIT = 6

res1 = 0
res2 = 0
res3 = 0
res4 = 0
TotalRes = {}
factor_List = []
counter = 0
#for number in range( 10 ** ( MAX_N_DIGIT - 1 ), 10 ** MAX_N_DIGIT ):
for number in range( 134043, 134050 ):
    counter += 1
    if counter == 1000:
        counter = 0
        print( number )

    if myMathHelper.IsPrime( number ):
        continue

    is_Found = False
    divisor_List = myMathHelper.GetAllDivisor( number )
    del divisor_List[0]
    for divisor in divisor_List:
        factor_List.clear()
        factor_List.append( divisor )
        factor_List.append( number // divisor )

        is_Exit = False
        while not is_Exit:
            for factor in factor_List:
                if myMathHelper.Is2Square( factor ):
                    continue
                if not myMathHelper.IsPrime( factor ):
                    sub_Factor_List = myMathHelper.GetAllDivisor( factor )
                    del sub_Factor_List[0]
                    factor_List.remove( factor )
                    factor_List.extend( sub_Factor_List )
                    if len( factor_List ) > MAX_N_DIGIT:
                        break

            is_Exit = True

        if len( factor_List ) != MAX_N_DIGIT:
            continue

        is_Valid = True
        for factor in factor_List:
            if factor != 2 and myMathHelper.Is2Square( factor ):
                if 2 in factor_List:
                    is_Valid = False
                    break
                else:
                    continue

            if not myMathHelper.IsPrime( factor ):
                is_Valid = False
                break

        if len(factor_List) != len( list( set(factor_List) ) ):
            is_Valid = False

        if not is_Valid:
            continue

        TotalRes[number] = list( factor_List )
        if res1 == 0:
            res1 = number
        elif res2 == 0:
            if number - res1 == 1:
                res2 = number
            else:
                res1 = number
        elif res3 == 0:
            if number - res2 == 1:
                res3 = number
                if MAX_N_DIGIT == 3:
                    is_Found = True
            else:
                res1 = number
                res2 = 0
        elif res4 == 0:
            if number - res3 == 1:
                res4 = number
                is_Found = True
            else:
                res1 = number
                res2 = 0
                res3 = 0
        break

    if is_Found:
        break

if MAX_N_DIGIT == 4 and res1 in TotalRes and res2 in TotalRes and res3 in TotalRes and res4 in TotalRes:
    print( '%d' % res1, end = ': ' )
    print( TotalRes[res1] )
    print( '%d' % res2, end = ': ' )
    print( TotalRes[res2] )
    print( '%d' % res3, end = ': ' )
    print( TotalRes[res3] )
    print( '%d' % res4, end = ': ' )
    print( TotalRes[res4] )
elif MAX_N_DIGIT == 3 and res1 in TotalRes and res2 in TotalRes and res3 in TotalRes:
    print( '%d' % res1, end = ': ' )
    print( TotalRes[res1] )
    print( '%d' % res2, end = ': ' )
    print( TotalRes[res2] )
    print( '%d' % res3, end = ': ' )
    print( TotalRes[res3] )
else:
    print( 'Not found!!!' )
    #print( TotalRes )
'''

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)

