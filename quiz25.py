import time

def GetFibNumber(pos):
    fib1 = 1
    fib2 = 1
    fib  = 0
    for i in range(3, pos + 1):
        fib = fib1 + fib2
        fib1, fib2 = fib2, fib    

    return fib

start_time = time.time()
count = 3
while len(str(GetFibNumber(count))) < 1000:
    count += 1

print(count)
elapsed_time = time.time() - start_time
print ("Elapse time: {:.2f} sec".format(elapsed_time))