from math import floor
from datetime import datetime

def IsPandigitalProducts(NumA, NumB, Product):
    strResult = str(NumA) + str(num_B) + str(Product)
    if len(strResult) != 9:
        return False
    for digit in str('123456789'):
        if not ( digit in strResult):
            return False

    return True
#----------------------------------------------------------- 

start_dt = datetime.now()
lst_ValidNum = []
lst_Products = []
for i in range(1, 5000):
    set_Digits = set()
    strDigit   = str(i)
    IsValid    = True
    for digit in strDigit:
        if not digit in set_Digits:
            set_Digits.add(digit)
        else:
            IsValid = False
            break
    if (IsValid == True):
        lst_ValidNum.append(i)
print(datetime.now() - start_dt)
print(len(lst_ValidNum))

start_dt = datetime.now()
sum_Result = 0
lst_Equation = []
for num_A in lst_ValidNum:    
    for num_B in lst_ValidNum:
        if num_A * num_B > 10000:
            break
        res = num_A * num_B
        if IsPandigitalProducts(num_A, num_B, res):
            lst_Temp = []
            lst_Temp.append(num_A)
            lst_Temp.append(num_B)
            lst_Temp.append(res)
            lst_Equation.append(lst_Temp)
            lst_Products.append(res)

print(datetime.now() - start_dt)
print(sum(set(lst_Products)))