number = 0
count = 0
for c in range(1, 6):
    value = int(input('Type a number: '))
    if value % 2 == 0:
        number += value
        count += 1
print('The sum of all {} even numbers is {}'.format(count, number))
