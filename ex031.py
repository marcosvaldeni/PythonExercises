travel = int(input('How many km will you travel? '))
print('You are about to take a {:.1f} Km journey.'.format(travel))
if travel <= 199:
    print('The cost of your ticket will cost R$ {:.2f}'.format(travel * 0.50))
else:
    print('The cost of your ticket will cost {:.2f}'.format(travel * 0.45))
