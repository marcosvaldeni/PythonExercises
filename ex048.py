sum = 0
count = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 == 1:
        sum += c
        count += 1
print('The sum of all {} numbers, that were requested is {}.'.format(count, sum))

