phrase = input('Type a phase: ').upper()
print('Your phrase has {} letters A '.format(phrase.count('A')))
print('The first letter A has a position at {}'.format(phrase.find('A')+1))
print('The last letter A has a position at {}'.format(phrase.rfind('A')+1))