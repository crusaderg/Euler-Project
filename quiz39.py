MIN_P_VALUE = 1
MAX_P_VALUE = 1001

perimeter_solutions = {} # Key is the perimeter of triangle, value is the list of solutions
solutions = []

exit_flag = False
for p in range( MIN_P_VALUE, MAX_P_VALUE ):
    exit_flag = False
    solutions = []
    for a in range( 1, 500 ):
        if ( exit_flag ):
            break

        for b in range( 1, 500 ):
            res1 = 2*a*p + 2*b*p - 2*a*b
            res2 = p*p
            if ( res1 == res2 ):
                for solution in solutions:
                    if ( a in solution ) and ( b in solution ):
                        exit_flag = True
                        break

                if ( exit_flag == True ):
                    break

                solutions.append( [ a, b, p - a - b ] )

    perimeter_solutions[p] = solutions

max_perimeter = 0
numberOfSolution = 0
for k, v in perimeter_solutions.items():
    if ( len(v) > numberOfSolution ):
        numberOfSolution = len(v)
        max_perimeter = k

print( "%s:" % ( max_perimeter ) )
print( "Solutions: " )
print( perimeter_solutions[ max_perimeter ] )  


'''
import math
import time

start_time = time.time()
sol = 0
dict = {}

for a in range(1, 500):
    for b in range(1, 500):
        c2 = math.pow(a,2) + math.pow(b,2)
        if int(c2**0.5)**2 == int(c2):
            p = a+b+int(math.sqrt(c2))
            if (p not in dict):
                dict[p] = 0
            else:
                dict[p] += 1

for k, v in dict.items():
    if v == max(dict.values()):
        sol = k

print('Solution: %s' % sol)
end_time=time.time()-start_time
print('Time: %s ' % end_time)
'''