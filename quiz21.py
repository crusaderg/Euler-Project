from math import sqrt

def GetAllDivisor(val):
    lst_Divisor = []
    for divisor in range(1, int((val/2)) + 1):
        if (val % divisor) == 0:
            lst_Divisor.append(divisor)

    return lst_Divisor
#-----------------------------------------------

sum_AmicableNum = 0
for i in range(1, 10000):
    sum_d1_lst = GetAllDivisor(i)
    if i == sum(GetAllDivisor(sum(sum_d1_lst))):
        print('%4d -> %4d' % (i, sum(sum_d1_lst)),end=' :')
        print(sum_d1_lst)
        if i != sum(sum_d1_lst):
            sum_AmicableNum += i

print('Sum of amicable numbers under 10000 is %d' % sum_AmicableNum)