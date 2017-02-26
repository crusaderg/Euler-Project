count = 0

lst_Compose = []
def ComposeToString(val1, val2, val3, val4, val5, val6, val7, val8):
    global count
    count += 1
#    if (count == 21):
#        exit()

    strCompose  = str(val1) + ' * ' + ' 2 Pound, '
    strCompose += str(val2) + ' * ' + ' 1 Pound, '
    strCompose += str(val3) + ' * ' + '50 Pence, '
    strCompose += str(val4) + ' * ' + '20 Pence, '
    strCompose += str(val5) + ' * ' + '10 Pence, '
    strCompose += str(val6) + ' * ' + ' 5 Pence, '
    strCompose += str(val7) + ' * ' + ' 2 Pence, '
    strCompose += str(val8) + ' * ' + ' 1 Pence '
    print(strCompose)
    lst_Compose.append(strCompose)
#----------------------------------------------------

def Sum_Money(val1, val2 = 0, val3 = 0, val4 = 0, val5 = 0, val6 = 0, val7 = 0, val8 = 0):
    return val1 * lst_Currency[1] \
                  + val2 * lst_Currency[2] \
                  + val3 * lst_Currency[3] \
                  + val4 * lst_Currency[4] \
                  + val5 * lst_Currency[5] \
                  + val6 * lst_Currency[6] \
                  + val7 * lst_Currency[7] \
                  + val8 * lst_Currency[8] 
#----------------------------------------------------

lst_Currency = [ 0, 200, 100, 50, 20, 10, 5, 2, 1 ]

total_C1  = total_C2 = total_C3 = total_C4 = \
total_C5  = total_C6 = total_C7 = total_C8 = 0
MAX_Money = 200
sum_Ways  = 0
sum_Temp  = 0
for c1 in range(0, 2):
    total_C1 = c1
    sum_Temp = Sum_Money( total_C1 )
    if sum_Temp == MAX_Money:
        sum_Ways += 1        
        ComposeToString( total_C1, total_C2, total_C3, total_C4,\
                         total_C5, total_C6, total_C7, total_C8 )
        continue
    for c2 in range(0, 3):
        total_C2 = c2
        sum_Temp = Sum_Money( total_C1, total_C2 )
        if sum_Temp == MAX_Money:
            sum_Ways += 1            
            ComposeToString( total_C1, total_C2, total_C3, total_C4,\
                             total_C5, total_C6, total_C7, total_C8 )
            continue
        elif sum_Temp > MAX_Money:
            total_C2 = 0
            break
        for c3 in range(0, 5):
            total_C3 = c3
            sum_Temp = Sum_Money( total_C1, total_C2, total_C3 )
            if sum_Temp == MAX_Money:
                sum_Ways += 1                
                ComposeToString( total_C1, total_C2, total_C3, total_C4,\
                                total_C5, total_C6, total_C7, total_C8)
                continue
            elif sum_Temp > MAX_Money:
                total_C3 = 0
                break
            for c4 in range(0, 11):
                total_C4 = c4
                sum_Temp = Sum_Money( total_C1, total_C2, total_C3, total_C4 )
                if sum_Temp == MAX_Money:
                    sum_Ways += 1                    
                    ComposeToString( total_C1, total_C2, total_C3, total_C4,\
                                    total_C5, total_C6, total_C7, total_C8)
                    continue
                elif sum_Temp > MAX_Money:
                    total_C4 = 0
                    break
                for c5 in range(0, 21):
                    total_C5 = c5
                    sum_Temp = Sum_Money( total_C1, total_C2, total_C3, total_C4, \
                                          total_C5 )
                    if sum_Temp == MAX_Money:
                        sum_Ways += 1                        
                        ComposeToString( total_C1, total_C2, total_C3, total_C4,\
                                        total_C5, total_C6, total_C7, total_C8)
                        continue
                    elif sum_Temp > MAX_Money:
                        total_C5 = 0
                        break
                    for c6 in range(0, 41):
                        total_C6 = c6
                        sum_Temp = Sum_Money( total_C1, total_C2, total_C3, total_C4, \
                                              total_C5, total_C6 )
                        if sum_Temp == MAX_Money:
                            sum_Ways += 1
                            total_C6  = c6
                            ComposeToString( total_C1, total_C2, total_C3, total_C4,\
                                            total_C5, total_C6, total_C7, total_C8)
                            continue
                        elif sum_Temp > MAX_Money:
                            total_C6 = 0
                            break
                        for c7 in range(0, 101):                            
                            total_C7 = c7
                            sum_Temp = Sum_Money( total_C1, total_C2, total_C3, total_C4, \
                                                  total_C5, total_C6, total_C7 )
                            if sum_Temp == MAX_Money:
                                sum_Ways += 1                                
                                ComposeToString( total_C1, total_C2, total_C3, total_C4,\
                                                total_C5, total_C6, total_C7, total_C8)
                                continue
                            elif sum_Temp > MAX_Money:
                                total_C7 = 0
                                break
                            for c8 in range(0, 201):
                                total_C8 = c8
                                sum_Temp = Sum_Money( total_C1, total_C2, total_C3, total_C4, \
                                                      total_C5, total_C6, total_C7, total_C8 )
                                if sum_Temp == MAX_Money:
                                    sum_Ways += 1                                    
                                    ComposeToString( total_C1, total_C2, total_C3, total_C4,\
                                                    total_C5, total_C6, total_C7, total_C8)
                                    continue
                                elif sum_Temp > MAX_Money:
                                    total_C8 = 0
                                    break

print(sum_Ways)
print(count)