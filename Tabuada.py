continuar = True
i = 0

while(continuar == True):
    num = int(input('Qual número você deseja ver a tabuada? - '))
    print()

    while(num < 0):
        num = int(input('Digite apenas números positivos - '))
        print()    

    while(i < 10):
        i += 1
        print(num,'.',i,'=',(i * num))

    print()
    print('Não - 0')
    print('Sim - 1')
    sim_nao = int(input('Deseja continuar? - '))
    print()

    if(sim_nao == 1):
        continuar = True
        i = 0
    elif(sim_nao == 0):
        continuar = False

