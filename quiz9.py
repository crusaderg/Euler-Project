from math import floor, sqrt
import time

TARGET_NUMBER = 1000

#------------------------------------------------------------------------
def foo1():
    for a in range(0, TARGET_NUMBER + 1):
        for b in range(a + 1,  TARGET_NUMBER + 1):
            square_c = a * a + b * b
            if floor(sqrt(square_c)) == sqrt(square_c):
                c = sqrt(square_c)
                if (a + b + c) == TARGET_NUMBER:
                    if (a < b) and (b < c):
                        print('product abc is %d' % (a * b * c) )
#------------------------------------------------------------------------

#------------------------------------------------------------------------
def foo2():
    for a in range(1, 333):
        for b in range(334, 668):
            if a**2 + b**2 == (1000 - a - b)**2:
                print('product abc is %d' % (a * b * (1000 - a - b)) )
#------------------------------------------------------------------------

t_Start = time.time()
foo1()
print('foo1 Elapsed %f' % (time.time() - t_Start))

t_Start = time.time()
foo2()
print('foo2 Elapsed %f' % (time.time() - t_Start))

print('Finish!!!')