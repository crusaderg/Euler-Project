import time 

start_time = time.time()

MAX_TRIANGLE_WORD_VALUE = ( ord('Z') - ord('A') + 1 ) * 26
word_index = 1
word_Value = 1
TRIANGLE_WORD_VALUES_SET = set()
while word_Value <= MAX_TRIANGLE_WORD_VALUE:
    TRIANGLE_WORD_VALUES_SET.add( word_Value )
    word_index += 1
    word_Value += word_index

LETTERS = {}
for i in range( ord('A'), ord('Z') + 1 ):
    LETTERS[ chr(i) ] = i - ord('A') + 1 

line = ''
with open( '/home/joe/study/python/Euler-Project/p042_words.txt', 'r' ) as wordFile:
    line = wordFile.readline()
words = line.replace( '"', '' ).split( ',' )

counter = 0
word_Value = 0
for word in words:
    word_Value = 0
    for letter in word:
        word_Value += LETTERS[ letter ]
    if word_Value in TRIANGLE_WORD_VALUES_SET:
        counter += 1

print( 'triangle words: %d' % counter )

elapsed_sec = time.time() - start_time
print('Time: %s ' % elapsed_sec)