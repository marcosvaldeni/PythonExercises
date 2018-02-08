number = int(input('Type a number: '))
count = 0
if number % 2 == 0:
    print('Number {} is not a prime number! Because it is even.'.format(number))
    count += 1
else:
    for c in range(3, (number-1)):
        if number % c == 0:
            print('NO,this number {} is not a prime number, it is divisible by {}'.format(number, c))
            count += 1
if count == 0:
    print('The number {} is a Prime number!'.format(number))
