shopping = float(input('How much was the shopping price? '))
print('Payment methods:')
print('[1] cash payment')
print('[2] credit card')
print('[3] 2x at credit card')
print('[4] 3x or more at credit card')
option = int(input('Which one do you pick? '))
if option == 1:
    print('Your purchase of the R$ {:.2f} will cost R$ {:.2f} at the end.'.format(shopping, shopping - (shopping * 0.1)))
elif option == 2:
    print('Your purchase of the R$ {:.2f} will cost R$ {:.2f} at the end.'.format(shopping, shopping - (shopping * 0.05)))
elif option == 3:
    print('Your purchase will be split into 2 installments of the {:.2f}'.format(shopping / 2))
elif option == 4:
    installments = int(input('How many installments? '))
    print('Your purchase will be split into {} installments of the R${:.2f}, the cost of R${:.2f} will increase to R${:.2f} at the end.'.format(installments, (shopping + (shopping * 0.2)) / installments, shopping, shopping + (shopping * 0.2)))
