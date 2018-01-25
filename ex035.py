a = float(input('Type a number to form a Triangle: '))
b = float(input('Type a number to form a Triangle: '))
c = float(input('Type a number to form a Triangle: '))

if (b - c) < a and a < (b + c) and (a - c) < b and b < a + c and (a - b) < c and c < (a + b):
    print('Yes, these three numbers cam form a Triangle!')
else:
    print('{}, {} and {} can not form a Triangle!'.format(a, b, c))

