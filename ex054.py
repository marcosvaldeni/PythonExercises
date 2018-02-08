from datetime import datetime
now = datetime.now()
person = []
ofage = 0
underage = 0
for c in range(1, 8):
    temp = int(input('In which year, the {}º was born? '.format(c)))
    person.insert(c-1, temp)
    if now.year - temp <= 18:
        ofage += 1
    else:
        underage += 1
print('At the total, we got {} person of age.'.format(ofage))
print('And also got {} person underage.'.format(underage))
