year = int(input('enter the year'))
div = year%4
if div==0:
    print('This year is a leap year')
else:
    print("this year is not a leap year")