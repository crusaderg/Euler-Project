from math import ceil, floor

def IsPalindrome(val):
    return val == val[::-1]
#----------------------------------------

sum_Result = 0
for num in range(1, 1000000):
    # check for the binary
    if IsPalindrome(str(num)) == False:
        continue

    strVal = "{0:b}".format(num)
    
    if IsPalindrome(strVal) == True:
        sum_Result += num

print(sum_Result)

# sum([x for x in range(1000000) if str(x)==str(x)[::-1] and bin(x)[2:]==bin(x)[:1:-1]])