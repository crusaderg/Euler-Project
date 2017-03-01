import math

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

def IsValid(strNum):
    for index in range(1, len(strNum)):
        # Check prime from left to right
        numVal = int(strNum[(-1 * index):])
        if IsPrime(numVal) == False:
            return False
        # Check prime from right to left
        numVal = int(strNum[0:(len(strNum) - index):])
        if IsPrime(numVal) == False:
            return False

    return True
#-------------------------------------------------------   

sum_Result = 0
lst_Result = []
for num in range(10, 1000001):
    if IsPrime(num) == False:
        continue
    
    if IsValid(str(num)) == True:       
        sum_Result += num
        lst_Result.append(num)
#-------------------------------------------------------  

print(sum_Result)
print(lst_Result)