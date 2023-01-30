num1 = int(input('Digite o número 1: '))
num2 = int(input('Digite o número 2: '))
num3 = int(input('Digite o número 3: '))

if(num1 > num2)and(num2 > num3):
    a = num1
    b = num2
    c = num3
elif(num1 > num3)and(num1 == num2):
    a = num1
    b = num2
    c = num3
elif(num1 > num3)and(num3 == num2):
    a = num1
    b = num3
    c = num2
elif(num1 > num3)and(num3 > num2):
    a = num1
    b = num3
    c = num2
elif(num1 > num2)and(num1 == num3):
    a = num1
    b = num3
    c = num2
elif(num2 > num1)and(num1 > num3):
    a = num2
    b = num1
    c = num3
elif(num2 > num3)and(num2 == num1):
    a = num2
    b = num1
    c = num3
elif(num2 > num3)and(num3 > num1):
    a = num2
    b = num3
    c = num1
elif(num2 > num1)and(num2 == num3):
    a = num2
    b = num3
    c = num1
elif(num2 > num1)and(num1 == num3):
    a = num2
    b = num1
    c = num3
elif(num3 > num1)and(num1 > num2):
    a = num3
    b = num1
    c = num2
elif(num3 > num2)and(num3 == num1):
    a = num3
    b = num1
    c = num2
elif(num3 > num2)and(num2 == num1):
    a = num3
    b = num2
    c = num1
elif(num3 > num2)and(num2 > num1):
    a = num3
    b = num2
    c = num1
elif(num3 > num1)and(num3 == num2):
    a = num3
    b = num2
    c = num1
else:
    print()
    print('Todos são iguais!')
    a = num1
    b = num2
    c = num3
    
print()
print(a, b, c)
print()

if((a ** 2) == ((b ** 2) + (c ** 2))):
    print('Triângulo Retângulo')
    if(a == b)and(b == c):
        print('Triângulo Equilátero')
    elif(a == b)or(b == c)or(a == c):
        print('Triângulo Isósceles')
    
elif((a ** 2) > ((b ** 2) + (c ** 2))):
    print('Triângulo Obtusângulo')
    if(a == b)and(b == c):
        print('Triângulo Equilátero')
    elif(a == b)or(b == c)or(a == c):
        print('Triângulo Isósceles')
        
elif((a ** 2) < ((b ** 2) + (c ** 2))):
    print('Triângulo Acutângulo')
    if(a == b)and(b == c):
        print('Triângulo Equilátero')
    elif(a == b)or(b == c)or(a == c):
        print('Triângulo Isósceles')

else:
    print('Não forma triângulo')
