n_pessoas = int(input('Digite a quantidade das pessoas na classe: '))

while(n_pessoas < 1):
    n_pessoas = int(input('Quantidade de pessoas impossível! Informe novamente: '))

print()

i = 0
soma_idade = 0

while(i < n_pessoas):
    i += 1

    idade = int(input('informe sua idade: '))

    while(idade < 0):
        idade = int(input('Idade incoerente! Informe novamente: '))

    soma_idade += idade

print()
media_idade = soma_idade / n_pessoas
print('Idade média da turma: %2.f' % media_idade)

print()

if(media_idade > -1)and(media_idade < 26):
    print('A classe é predominantemente JOVEM')
elif(media_idade > 25)and(media_idade < 61):
    print('A classe é predominantemente ADULTA')
elif(media_idade > 60):
    print('A classe é predominantemente IDOSA')
else:
    print('Valor inesperado ou incoerente!')
