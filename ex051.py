print('='*40)
print('10 SEQUENCER OF A ARITHMETIC PROGRESSION')
print('='*40)
start = int(input('First term: '))
ratio = int(input('Ratio: '))
for c in range(start, 10):
    print(start, end=' → ')
    start += ratio
print('The End')
