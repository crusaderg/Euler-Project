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

res_A = 0
res_B = 0
max_n = 0
n     = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        tmp_product = (n ** 2) + (a * n) + b        
        while((tmp_product > 0) and IsPrime(tmp_product)):
            n += 1
            tmp_product = (n ** 2) + (a * n) + b
        if (n > max_n):
            max_n = n
            res_A = a
            res_B = b

print('a: %d, b: %d, max_n: %d, product: %d' % (res_A, res_B, max_n, res_A * res_B))