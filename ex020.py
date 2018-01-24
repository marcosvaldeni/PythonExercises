import random
student1 = str(input('First student: '))
student2 = str(input('Second student: '))
student3 = str(input('Third student: '))
student4 = str(input('Fourth student: '))
student5 = str(input('Fifth student: '))
students = [student1, student2, student3, student4, student5]
random.shuffle(students)
print('The presentation order will be: ')
print(students)

