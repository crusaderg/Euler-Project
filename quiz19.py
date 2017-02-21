from math import floor, ceil

def IsLeapYear(val):
    if (val % 100) == 0:
        if (val % 400) == 0:
            return True
        else:
            return False
    if (val % 4) == 0:
        return True

    return False
#------------------------------------------------------

def GetMonthDay(yearVal, monthVal):
    if monthVal in [1,3,5,7,8,10,12]:
        return 31
    if monthVal in [4,6,9,11]:
        return 30
    if IsLeapYear(yearVal):
        return 29

    return 28
#------------------------------------------------------

# Week day from Monday to Sunday: 1 to 7
weekDayOfFirstDay    = 2
sum_FirstDayIsSunday = 0
for yearNum in range(1901, 2001):
    for monthNum in range(1, 13):
        print('Year %d Month %d, weekday %d' % (yearNum, monthNum, weekDayOfFirstDay))
        if (weekDayOfFirstDay == 7):
            sum_FirstDayIsSunday += 1
        # Calculate the weekday of the first day of next month
        monthDay = GetMonthDay(yearNum, monthNum)
        weekDayOfFirstDay += monthDay % 7
        if (weekDayOfFirstDay > 7):
            weekDayOfFirstDay = weekDayOfFirstDay % 7


print('Total First day of a month is Sunday from 1900 to 2000 is %d' % sum_FirstDayIsSunday)