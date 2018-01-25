salary = float(input('What is the employee salary? R$ '))
if salary >= 1250:
    print('A employee that was making R$ {:.2f}, with 10% of increasing will make R$ {:.2f}'.format(salary, (salary * 0.10) + salary))
else:
    print('A employee that was making R$ {:.2f}, with 15% of increasing will make R$ {:.2f}'.format(salary, (salary * 0.15) + salary))
