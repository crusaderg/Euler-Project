from math import floor

str_1_To_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 
               'seven', 'eight', 'nine', 'ten', 'eleven', 'tweleve', 
               'thirteen', 'fourteen', 'fiveteen', 'sixteen', 
               'seventeen', 'eighteen', 'nineteen']
str_20_To_90 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty'
                'seventy', 'eighty', 'ninety']
str_100  = 'hundred'
str_1000 = 'thousand'
str_And  = 'and'

MAX_NUMBER = 1000
sum_Letter = 0

print(len(str_20_To_90))
for num in range(1, MAX_NUMBER + 1):
    if num < 20:
        sum_Letter += len(str_1_To_19[num])
    if num >= 20 and num <= 99:
        sum_Letter += len(str_1_To_19[num % 10])
        sum_Letter += len(str_20_To_90[ floor(num / 10) ])
    if num >= 100 and num <= 999:
        sum_Letter += len(str_1_To_19[ floor(num / 100) ]) + len(str_100)
        sum_Letter += str_And
        digit = num % 100
        sum_Letter += len(str_1_To_19[digit % 10])
        sum_Letter += len(str_20_To_90[ floor(digit / 10) ])
   
sum_Letter += len(str_1_To_19[1]) + len(str_1000)

print('Totsl sum of letters is %d' % sum_Letter)