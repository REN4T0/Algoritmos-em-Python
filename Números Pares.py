print()
n1 = int(input('Digite o número inicial: '))
n2 = int(input('Até qual número você deseja saber os pares? - '))
print()

i = 0

if(n1 < n2):
    while(n1 < n2):
        n1 += 1

        if(n1 % 2 == 0):
            i += 1
            print(n1)

elif(n1 > n2):
    while(n1 > n2):
        n1 -= 1

        if(n1 % 2 == 0):
            i += 1
            print(n1)

print()
print('Quantidade de números pares: ', i)
