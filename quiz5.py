

#-----------------------------------------------
def foo1():
    val = 739024 * 2520
    small_Multiple = 739024 * 2520
    lst_Factor = list(range(11,21))
    while(True):
        isFound = True
        if (val % lst_Factor[-1]) != 0:
            if (val % lst_Factor[-1]) != 0:
                val = val - (val % lst_Factor[-1])
            else:
                val = val - lst_Factor[-1]
            
            if (val < 2520):
                break
            continue
        
        for i in lst_Factor:
            if (val % i) == 0:
                continue
            isFound = False
            break

        if (isFound == True):
            print('found %d' % val)
            if (val < small_Multiple):
                small_Multiple = val

        val = val - 1  

    print('Smallest multiple is %d' % small_Multiple)
#-----------------------------------------------

#-----------------------------------------------
def foo2():
    primeFactor = 2*3*5*7*11*13*17*19
    lst_Factor  = list(range(11,21))
    val         = primeFactor

    while(True):
        isFound = True
        for i in lst_Factor:
            if (val % i) == 0:
                continue
            isFound = False
            break
        
        if (isFound == True):
            print('Smallest multiple is %d' % val)
            break

        val = val + primeFactor
#-----------------------------------------------

foo2()