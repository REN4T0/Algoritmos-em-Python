from random import randint

i = randint(0,20)
a = 0

n = int(input('Digite um número: '))
print()

while(True):
    i = randint(1,20)

    if(i != n):
        print(i, end = ', ')
    elif(i == n):
        print(i, end = '.')
        

    a += i
    
    if(i == n):
        break

print()
print()
print('Soma de todos os números aleatórios gerados: ', a)
    
