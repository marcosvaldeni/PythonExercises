import random
from time import sleep

print('-=-'*30)
print('COMPUTER: I will think about a number, between 0 to 5. Try to guess...')
print('-=-'*30)
number = random.randint(0, 5)
guess = input('Which number did I pick? ')
print('PROCESSING...')
sleep(3)
if guess == number:
    print('You winn! The number I was thinking is {}'.format(number))
else:
    print('I winn, I was thinking about the number {}'.format(number))
