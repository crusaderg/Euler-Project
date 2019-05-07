import time 

start_time = time.time()

pentagon_List = []
for n in range( 1, 10001 ):
    number = ( n * ( 3 * n - 1 ) ) / 2
    pentagon_List.append( int(number) )

pentagon_Set = set(pentagon_List)

found = False
for j in pentagon_List:
    for k in pentagon_List:
        if j == k:
            continue
        
        if ( abs( j - k ) in pentagon_Set ) and ( ( j + k ) in pentagon_Set ):
            print( abs( j - k ) )
            found = True
            break
    if found == True:
        break
        
elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)