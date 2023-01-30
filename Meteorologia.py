print("DEPARTAMENTO ESTADUAL DE METEOROLOGIA")
print()

soma_temperatura = 0
sim = 'S'
nao = 'N'
maior = 0
menor = 0
i = 0

while(True):
    i += 1
    
    temperatura = float(input('Digite a temperatura indicada em celsius (°C): '))

    soma_temperatura += temperatura

    if(i == 1):
        menor = temperatura
        maior = temperatura

    if(temperatura > maior):
        maior = temperatura
    elif(temperatura < menor):
        menor = temperatura

    print()

    print('Não - N')
    print('Sim - S')
    sim_nao = str(input('Deseja continuar? - '.upper))

    while(sim_nao != 'N')or(sim_nao != 'S'):
        print('Comando não identificado! Digite apenas o que está sendo sugerido abaixo!')
        print()
        print('Não - Digite N')
        print('Sim - Digite S')
        sim_nao = str(input('Deseja continuar? - '.upper))

    if(sim_nao == 'N'):
        break
            
    print()

media_temperatura = soma_temperatura / i

print('Maior temperatura informada:',maior,'°C')
print('Menor temperatura informada:',menor,'°C')
print('Média das temperaturas informadas: %.1f' % media_temperatura,'°C')


