first = float(input('First score: '))
second = float(input('Second score: '))
grade = (first + second) / 2
print('Getting {} and {}, the final grade will be {}'.format(first, second, (first+second) / 2))
if grade >= 7:
    print('The student has passed!')
elif 5 <= grade < 7:
    print('the student in recovery.')
else:
    print('The student FAILED!')
