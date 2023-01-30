num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))

if(num1 > num2) and (num1 > num3):
    print('Número maior: ', num1)
elif(num2 > num1) and (num2 > num3):
    print('Número maior: ', num2)
elif(num3 > num1) and (num3 > num2):
    print('Número maior: ', num3)
else:
    print('Todos os números são iguais!')
