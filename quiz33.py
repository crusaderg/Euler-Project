from math import floor

dic_ValidResult = {}
for numerator in range(1, 10):
    for denominator in range(1,10):
        res = numerator / denominator
        if res >= 1:
            continue
        dic_ValidResult[res] = 0

lst_Result = []
product_Numerator   = 1
product_Denominator = 1
for numerator in range(11, 100):
    if numerator % 10 == 0:
        continue
    tmpNumerator   = 0
    tmpDenominator = 0
    for denominator in range(11,100):
        if not ((numerator / denominator) in dic_ValidResult):
            continue
        
        IsValid = False
        if floor(numerator / 10) == floor(denominator / 10):
            tmpNumerator   = numerator % 10
            tmpDenominator = denominator % 10
            if tmpDenominator == 0:
                continue
            if tmpNumerator / tmpDenominator >= 1:
                continue
            IsValid = True
        if floor(numerator / 10) == (denominator % 10):
            tmpNumerator   = numerator % 10
            tmpDenominator = floor(denominator / 10)
            if tmpDenominator == 0:
                continue
            if tmpNumerator / tmpDenominator >= 1:
                continue
            IsValid = True
        if (numerator % 10) == floor(denominator / 10):
            tmpNumerator   = floor(numerator / 10)
            tmpDenominator = denominator % 10
            if tmpDenominator == 0:
                continue
            if tmpNumerator / tmpDenominator >= 1:
                continue
            IsValid = True
        if (numerator % 10) == (denominator % 10):
            tmpNumerator   = floor(numerator / 10)
            tmpDenominator = floor(denominator / 10)
            if tmpDenominator == 0:
                continue
            if tmpNumerator / tmpDenominator >= 1:
                continue
            IsValid = True
        
        if (denominator != 0) and (tmpDenominator != 0):            
            if (numerator / denominator) != (tmpNumerator / tmpDenominator):
                IsValid = False

        if IsValid == True:
            lst_Temp = []
            lst_Temp.append(numerator)
            lst_Temp.append(denominator)
            lst_Result.append(lst_Temp)
            product_Numerator   *= numerator
            product_Denominator *= denominator

print(lst_Result)
print(1 / (product_Numerator / product_Denominator))