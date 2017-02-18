MAX_NUMBER = 1000
sum = 0

for number in range(1, MAX_NUMBER):
    if ((number % 3) == 0) or ((number % 5) == 0):
        sum = sum + number

print("sum = $1\n" , (sum))        