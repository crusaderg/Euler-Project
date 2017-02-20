from math import floor

str_1_To_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 
               'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 
               'thirteen', 'fourteen', 'fifteen', 'sixteen', 
               'seventeen', 'eighteen', 'nineteen']
str_20_To_90 = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
                'seventy', 'eighty', 'ninety']
str_100  = 'hundred'
str_1000 = 'thousand'
str_And  = 'and'

MAX_NUMBER = 1000
sum_Letter = 0
str_Number = ''

for num in range(1, MAX_NUMBER):
    str_Number = ''
    if num < 20:
        sum_Letter += len(str_1_To_19[num])
        str_Number += str_1_To_19[num] + ' '
    if num >= 20 and num <= 99:
        sum_Letter += len(str_20_To_90[ floor(num / 10) ])
        str_Number += str_20_To_90[ floor(num / 10) ] + ' '
        sum_Letter += len(str_1_To_19[num % 10])
        str_Number += str_1_To_19[num % 10] + ' '
    if num >= 100 and num <= 999:
        sum_Letter += len(str_1_To_19[ floor(num / 100) ]) + len(str_100)
        str_Number += str_1_To_19[ floor(num / 100) ] + ' '
        str_Number += str_100 + ' '
        digit = num % 100
        if (digit == 0):
            print('Number %d: %s' % (num, str_Number))
            continue
        sum_Letter += len(str_And)
        str_Number += str_And + ' '
        if digit < 20:
            sum_Letter += len(str_1_To_19[digit])
            str_Number += str_1_To_19[digit] + ' '
        else:
            sum_Letter += len(str_20_To_90[ floor(digit / 10) ])
            str_Number += str_20_To_90[ floor(digit / 10) ] + ' '
            sum_Letter += len(str_1_To_19[digit % 10])
            str_Number += str_1_To_19[digit % 10] + ' '
    print('Number %d: %s' % (num, str_Number))
   
sum_Letter += len(str_1_To_19[1]) + len(str_1000)

print('Totsl sum of letters is %d' % sum_Letter)