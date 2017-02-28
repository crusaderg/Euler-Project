from math import factorial

sum_Result = 0
lst_Result = []
for i in range(3, 1000000):
    strNum   = str(i)
    sum_Temp = 0
    for num in strNum:
        sum_Temp += factorial(int(num))
        if sum_Temp > i:
            break
    if sum_Temp == i:
        sum_Result += i
        lst_Result.append(i)

print(sum_Result)
print(lst_Result)