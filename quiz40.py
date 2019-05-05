import time

start_time = time.time()

MIN_SINGLE_DIGIT   = 1
MAX_SINGLE_DIGIT   = 9
MIN_DOUBLE_DIGIT = 10
MAX_DOUBLE_DIGIT = 99
MIN_THREE_DIGIT  = 100
MAX_THREE_DIGIT  = 999
MIN_FOUR_DIGIT   = 1000
MAX_FOUR_DIGIT   = 9999

DIGHT_INDEX = [ 1, 10, 100, 1000, 10000, 100000, 1000000 ]

# Test purpose
string_Value = ''
for i in range( MIN_SINGLE_DIGIT, MAX_SINGLE_DIGIT + 1 ):
    string_Value += str( i )

for i in range( MIN_DOUBLE_DIGIT, MAX_DOUBLE_DIGIT + 1 ):
    string_Value += str( i )

for i in range( MIN_THREE_DIGIT, MAX_THREE_DIGIT + 1 ):
    string_Value += str( i )

for i in range( MIN_FOUR_DIGIT, MAX_FOUR_DIGIT + 1 ):
    string_Value += str( i )

print( '1st    digit is %s' % ( string_Value[ 0 ] ) )
print( '10st   digit is %s' % ( string_Value[ 9 ] ) )
print( '12th   digit is %s' % ( string_Value[ 11 ] ) )
print( '100th  digit is %s' % ( string_Value[ 99 ] ) )
print( '1000th digit is %s' % ( string_Value[ 999 ] ) )

n_Digit_Start_Index  = {} # key is the length of dights, value is the start index of each single-dight, double-dight etc
n_Digit_Length       = {} # key is the length of dights, value is the lengthx of each single-dight, double-dight etc
n_Digit_Value        = {} # key is the index of dights, value is the value of it
# Caculate n length digit start index
current_digit_length = 0
n = 0
for i in DIGHT_INDEX:
    while current_digit_length < i:
        n += 1
        n_digit_length = 9 * ( 10 ** ( n - 1) ) * n
        current_digit_length += n_digit_length

    n_Digit_Start_Index[n] = current_digit_length - n_digit_length + 1
    n_Digit_Length[n]      = n_digit_length

print( 'n_Digit_Start_Index:', end = ' ' )
print( n_Digit_Start_Index )
print( 'n_Digit_Length:', end = ' ' )
print( n_Digit_Length )

# Caculate digit of index
n = 1
for index in DIGHT_INDEX:    
    while index >= ( n_Digit_Start_Index[n] + n_Digit_Length[n] ):
        n += 1
    
    offset = index - n_Digit_Start_Index[n]
    #print( 'index: %d, n: %d, offset: %d' % ( index, n, offset )  )
    number_offset = offset // n
    digit_offset  = offset % n
    number = 10 ** (n - 1) + number_offset
    #print( 'number: %d, digit_offset: %d' % ( number, digit_offset )  )
    n_Digit_Value[index] = str(number)[digit_offset]

print( n_Digit_Value )

# Caulate the result
result = 1
for k, v in n_Digit_Value.items():
    result *= int(v)

print( 'reslult = %d' % result )

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)
