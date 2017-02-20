MAX_POWER = 1000

strRes = str(2**MAX_POWER)

sum_Power = 0
for i in strRes:
    sum_Power += int(i)

print('Power digit sum: %d' % sum_Power)