height = float(input('What is your height? '))
weigh = float(input('How much do you weigh? '))
imc = weigh / (height * height)
print('The IMC is {:.2f}'.format(imc))
if 18.5 > imc:
    print('Underweight')
elif 18.5 <= imc < 25:
    print('Normal Weight')
elif 25 <= imc < 30:
    print('Overweight')
elif 30 <= imc < 40:
    print('Obesity')
elif 40 < imc:
    print('Morbid Obesity')
