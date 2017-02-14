from math import floor,sqrt,ceil
import time

OVER_DIVISOR = 500

#-------------------------------------
def GetTriangleNumber(pos):
    if (pos == 1):
        return 1

    if (pos % 2) == 0:
        return (1 + pos) * (pos / 2)
    
    prePos = pos - 1
    return ((1 + prePos) * (prePos / 2)) + pos     
#-------------------------------------

#-------------------------------------
def GetDivisorsCount(val):
    divisor_Count = 1
    for i in range(2, floor(val / 2) + 1):
        if (val % i) == 0:
            divisor_Count += 1
    
    return divisor_Count + 1

def find_divisors(number):
    divisors = 0
    sqrtNum = ceil(sqrt(number))
    for i in range(1, int(sqrtNum)):
        if number % i == 0:
            divisors += 1
    return divisors*2    
#-------------------------------------

pos = 1
tm_Start = time.time()
triangleNumber = 0
divisor_Count  = 0
while (True):
    triangleNumber = GetTriangleNumber(pos)
#    divisor_Count  = GetDivisorsCount(triangleNumber)
    divisor_Count  = find_divisors(triangleNumber)
    if (divisor_Count > OVER_DIVISOR):
        print('Highly divisible triangular number: %d' % triangleNumber)
        break

    pos += 1

#print('%d %d %d' % (pos - 1, GetTriangleNumber(pos - 1), GetDivisorsCount(GetTriangleNumber(pos - 1))))
print('%d %d %d' % (pos, triangleNumber, divisor_Count))
print('Elapsed %d seconds...' % (time.time() - tm_Start))