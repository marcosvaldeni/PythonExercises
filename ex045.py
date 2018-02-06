import random
print('[1] Rock')
print('[2] Paper')
print('[3] Scissors')
objects = ['Rock', 'Paper', 'Scissors']
player = int(input('Do you want to try? '))
computer = random.randint(1, 3)
print('Computer has chosen {}'.format(objects[computer-1]))
if player == 1 and computer == 1:
    print('Draw')
elif player == 2 and computer == 1:
    print('You win!')
elif player == 3 and computer == 1:
    print('Computer win!')
elif player == 1 and computer == 2:
    print('Computer win!')
elif player == 1 and computer == 3:
    print('Computer win!')
elif player == 2 and computer == 2:
    print('Draw')
elif player == 2 and computer == 3:
    print('Computer win!')
elif player == 3 and computer == 2:
    print('You win!')
elif player == 3 and computer == 3:
    print('Draw')
