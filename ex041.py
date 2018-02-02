from datetime import datetime
now = datetime.now()
year = int(input('Year of birth: '))
age = now.year - year
print('The athlete is {} years old.'.format(age))
if age <= 9:
    print('Classification: Kid')
elif 9 < age <= 14:
    print('Classification: Young')
elif 14 < age <= 19:
    print('Classification: Junior')
elif 19 < age <= 25:
    print('Classification: Senior')
elif 25 < age:
    print('Classification: Master')

