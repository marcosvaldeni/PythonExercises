a = float(input('Type a number to form a Triangle: '))
b = float(input('Type a number to form a Triangle: '))
c = float(input('Type a number to form a Triangle: '))

if (b - c) < a and a < (b + c) and (a - c) < b and b < a + c and (a - b) < c and c < (a + b):
    if a == b and a == c:
        print('These three numbers cam form a Equilateral Triangle!')
    elif a == b or a == c or b == c:
        print('These three numbers cam form a Isosceles Triangle!')
    else:
        print('These three numbers cam form a Scalene Triangle!')
else:
    print('{}, {} and {} can not form a Triangle!'.format(a, b, c))
