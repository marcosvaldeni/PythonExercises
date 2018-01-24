import math
opposide = float(input('Length of opposide leg: '))
adjacent = float(input('Length of adjacent leg: '))
print('The hypotenuse will be: {:.2f}'.format(math.sqrt((math.pow(opposide, 2))+(math.pow(adjacent, 2)))))
# print('The hypotenuse will be: {:.2f}'.format(math.hypot(opposide, adjacent)))
