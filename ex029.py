speed = int(input('How fast is your car? '))
if speed > 80:
    print('Taxed! You were taxed for driving above the speed limit, that is 80Km/h')
    print('You have to pay a tax of the R${:.2f}'.format((speed-80)*7))
else:
    print('Drive safely!')
