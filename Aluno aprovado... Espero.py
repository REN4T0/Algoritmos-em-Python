i = 0
soma = 0

while i < 3:
    i += 1
    
    print('Digite a nota', (i))
    nota = float(input())

    soma += nota

media = soma / i

if(media < 51):
    print('Média:%.2f' % media,'- O aluno está REPROVADO!')
elif(media > 50) and (media < 70):
    print('Média:%.2f' % media,'- O aluno está de RECUPERAÇÃO!')
else:
    print('Média:%.2f' % media,'- O aluno está APROVADO!')
