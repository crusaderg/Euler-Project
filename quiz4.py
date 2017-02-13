#----------------------------------------
def IsPalinedrome(val):
    strVal = str(val)
    strVal = strVal[::-1]
    newVal = int(strVal)
    if (newVal == val):
        return True

    return False
#----------------------------------------

lstRange  = list(range(100, 1000))
lstRange.reverse()

max_Palinedrome = 0
digitNumVal1    = 0
digitNumVal2    = 0
for digitNum1 in lstRange:
    for digitNum2 in lstRange:
        if (IsPalinedrome(digitNum1 * digitNum2) == True):
            if ((digitNum1 * digitNum2) > max_Palinedrome):
                max_Palinedrome = digitNum1 * digitNum2
                digitNumVal1    = digitNum1
                digitNumVal2    = digitNum2

print('Max palinedrome is %d' % max_Palinedrome)
print('num1 is %d, num2 is %d' % (digitNumVal1, digitNumVal2))