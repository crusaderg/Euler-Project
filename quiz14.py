START_NUMBER = 1000000

#----------------------------------------------
def GenerateChain(val):
    if (val % 2) == 0:
        return int(val / 2)

    return val * 3 + 1
#----------------------------------------------

longest_Chain = []
lstChain      = [START_NUMBER]
for i in range (1, START_NUMBER + 1):
    res      = i
    lstChain = [i]
    while res != 1:
        res = GenerateChain(int(res))
        lstChain.append(res)
    if len(lstChain) > len(longest_Chain):
        longest_Chain = lstChain

print(longest_Chain[0])
#print(longest_Chain[0])