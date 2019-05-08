import time 

start_time = time.time()

triangle_List   = []
pentagonal_List = []
pentagonal_Set  = set()
hexagonal_List  = []
hexagonal_Set   = set()

for n in range( 1, 100001 ):
    triangle_List.append( n * ( n + 1 ) / 2 )
    pentagonal_List.append( n * ( 3 * n - 1 ) / 2 )
    hexagonal_List.append( n * ( 2 * n - 1 ) )

pentagonal_Set = set( pentagonal_List )
hexagonal_Set  = set( hexagonal_List )

filter_set = set( [ 1, 40755 ] )

for number in triangle_List:
    if ( number in pentagonal_Set ) and ( number in hexagonal_Set ) and ( not number in filter_set ):
        print( number )
        break

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)