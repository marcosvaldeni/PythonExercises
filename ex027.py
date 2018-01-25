name = input('Type your full name: ')
names = name.split()
print('It is a pleasure to meet you!')
print('Your fist name is {}'.format(names[0]))
print('Your surname is {}'.format(names[len(names)-1]))

