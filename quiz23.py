#-------------------------------------------------------
def GetAllDivisor(val):
    lst_Divisor = []
    for divisor in range(1, int((val/2)) + 1):
        if (val % divisor) == 0:
            lst_Divisor.append(divisor)

    return lst_Divisor
#-------------------------------------------------------

#-------------------------------------------------------
def IsAbundantNumber(val):
    lst_Divisor = GetAllDivisor(val)
    if sum(lst_Divisor) > val:
        return True

    return False
#-------------------------------------------------------

map_AbundantNum = {}
for num in range(12, 28124):
    if IsAbundantNumber(num) == True:
        map_AbundantNum[num] = 0

print('Start to check for the sum of none abundant num...')
sum_Result = 0
for i in range(13, 28124):
    foundAnotherAbundantNum = False
    for abundantNum in map_AbundantNum:
        if (i - abundantNum) in map_AbundantNum:
            foundAnotherAbundantNum = True
            break
    if (foundAnotherAbundantNum == False):
        sum_Result += i

print(sum_Result + sum(range(1, 13)))