number1 = float(input('Type first number: '))
number2 = float(input('Type second number: '))
number3 = float(input('Type third number: '))

if number1 > number2:
    biggest = number1
else:
    biggest = number2

if biggest < number3:
    biggest = number3

if number1 < number2:
    lowest = number1
else:
    lowest = number2

if lowest > number3:
    lowest = number3

print('The biggest number was {:.0f}'.format(biggest))
print('The lowest number was {:.0f}'.format(lowest))
