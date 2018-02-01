from datetime import datetime
now = datetime.now()
year = int(input('Year of birth: '))
age = now.year - year
print('Who was born in {} is {} years old in {}.'.format(year, now.year - year, now.year))

if age == 18:
    print('You must enlist immediately!')
elif age > 18:
    print('You should already have enlisted for {} years.'.format(now.year - (year + 18)))
    print('Your enlisted was in {}.'.format(year + 18))
else:
    print('It still has {} years left for your enlistment'.format(now.year - (year + 18)))
    print('Your enlisted will be in {}.'.format(year + 18))
