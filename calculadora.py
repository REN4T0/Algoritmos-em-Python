num1 = float(input('Digite um número: '))
sinal = str(input('Digite um símbolo operacional(+),(-),(*),(/): '))
num2 = float(input('Digite um número: '))

if(sinal == '+'):
    result = num1 + num2
elif(sinal == '-'):
    result = num1 - num2
elif(sinal == '*'):
    result = num1 * num2
elif(sinal == '/'):
    while(num2 == 0):
        num2 = float(input('Impossível dividir por zero! Digite outro número: '))
    result = num1 / num2
else:
    if(sinal != '+', '-', '*', '/'):
        print('Sinal não identificado!')
    else:
        print(result)

print(result)
