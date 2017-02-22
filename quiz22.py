lst_Name = []
with open("C:\\workShop\\GitHub\\p022_names.txt") as NamesFile:
    for line in NamesFile:
        lst_Name = [name.strip('"') for name in line.split(',')]

lst_Name.sort()
sum_AllNames = 0
for i in range(0, len(lst_Name)):
    name = lst_Name[i]
    sum_Letter = 0
    for letter in name:
        sum_Letter += ord(letter) - ord('A') + 1
    sum_AllNames += sum_Letter * (i + 1)

print(sum_AllNames) 