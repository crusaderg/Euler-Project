from math import sqrt

MAX_NATURALNUMBER = 100 + 1
sum = 0
square_sum = 0
for i in range(1, MAX_NATURALNUMBER):
    sum += i
    square_sum += i**2

print('Sum square difference %d' % (sum**2 - square_sum))