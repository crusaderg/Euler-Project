lst_Result = []
for a in range(2, 101):
    for b in range(2, 101):
        if not ((a ** b) in lst_Result):
            lst_Result.append(a ** b)

#lst_Result.sort()
print(len(lst_Result))