number = int(input('Table: '))
for c in range(1, 11):
    print('{:2} x {} = {:2}'.format(c, number, c * number))
