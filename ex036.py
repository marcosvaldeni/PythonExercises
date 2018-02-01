house = float(input('How much is the house? R$ '))
salary = float(input('How much is the buyer\'s salary? R$ '))
years = int(input('How many years of funding? '))
months = years * 12
installments = house / months
print('To pay a house of R$ {:.2f} in {} years the installment will be {:.2f} per month.'.format(house, years, installments))
if (salary * 0.30) >= installments:
    print('Loan cam be granted!')
else:
    print('Loan denied!')
