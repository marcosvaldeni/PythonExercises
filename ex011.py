height = float(input('Type the height of wall: '))
width = float(input('Type the width of wall: '))
mSquared = height * width
print('Your wall has the dimension of {}x{} and the squared area is {}²'.format(height, width, mSquared))
print('To paint this wall, you will need {}l of ink.'.format(mSquared/2))
