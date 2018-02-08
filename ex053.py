phrase = str(input('Type a phrase: ')).upper()
phrase = phrase.replace(' ', '')
iPhrase = phrase[::-1]
print('The inverse of {} is {}'.format(phrase, iPhrase))
if iPhrase == phrase:
    print('The typed phrase is a palindrome!')
else:
    print('The typed phrase is not a palindrome.')
