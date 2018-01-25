year = int(input('Type a year to check if it a leap year: '))
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print('Yes, {} is a leap year.'.format(year))
else:
    print('No, {} is not a leap year.'.format(year))