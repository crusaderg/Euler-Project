import math

strVal = str(math.factorial(100))

sum_Digits = 0
for intVal in strVal:
    sum_Digits += int(intVal)

print(sum_Digits)