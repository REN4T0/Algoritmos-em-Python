velocidade = float(input('Informe a velocidade do veículo: '))

multa1 = 129
multa2 = 257
multa3 = 490

ponto1 = 2
ponto2 = 4
ponto3 = 7

if(velocidade > 50)and(velocidade < 60):
    print('Você foi autuado por excesso de velocidade!')
    print('Valor da multa: R$%.2f' % multa1)
    print('Pontos na carteira: ', ponto1)
elif(velocidade > 59)and(velocidade < 80):
    print('Você foi autuado por excesso de velocidade!')
    print('Valor da multa: R$%.2f' % multa2)
    print('Pontos na carteira: ', ponto2)
elif(velocidade > 79):
    print('Você foi autuado por excesso de velocidade!')
    print('Valor da multa: R$%.2f' % multa3)
    print('Pontos na carteira: ', ponto3)
else:
    print('Velocidade permitida dentro das normas de trânsito! Sem necessidade de multas e pontos.')
