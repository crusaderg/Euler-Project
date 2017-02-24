lst_Number = []

for num in range(1000, 1000000):
    strNumber = str(num)
    sum_Num   = 0
    for i in strNumber:
        sum_Num += int(i) ** 5
        if (sum_Num > num):
            break
    if (sum_Num == num):
        lst_Number.append(num)

print(lst_Number)
print(sum(lst_Number))