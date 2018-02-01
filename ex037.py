number = int(input('Type a number: '))
print('Choose one of the bases for conversion: ')
print('[1] Convert to Binary:')
print('[2] Convert to Octal:')
print('[3] Convert to Hexadecimal:')
choice = int(input('Your choice: '))
if choice == 1:
    print('Binary: {}'.format(bin(number)[2:]))
elif choice == 2:
    print('Octal {}'.format(oct(number)[2:]))
elif choice == 3:
    print('Hexadecimal {}'.format(hex(number)[2:]))

