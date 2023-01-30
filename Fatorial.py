num = int(input('Digite um número a ser fatoriado: '))
print()

while(num < 0):
    num = int(input('É impossível fatoriar números negativos! Digite outro número: '))
    print()

fatorial = 1

while(num > 0):
    num -= 1

    if(num > 0):
        print(num + 1, end = ' . ')
    elif(num < 1):
        print(num + 1, end = ' = ')

    fatorial = fatorial * (num + 1)

print(fatorial)



    
