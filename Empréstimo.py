valor_casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salário: '))
tempo_pagar = int(input('Em quantos meses você pretende pagar a prestação? - '))

trintaporcent_salario = salario * 0.3
prestacao_mensal = valor_casa / tempo_pagar

print()

if(prestacao_mensal > trintaporcent_salario):
    print('CADASTRO NÃO APROVADO!')
    print()
    print('A prestação mensal é maior que 30% do seu salário.')
    print()
    print('DADOS')
    print('Valor do salário: R$%.2f' % salario)
    print('Valor do empréstimo: R$%.2f' % valor_casa)
    print('Tempo a pagar:', tempo_pagar, 'meses')
    print('30 porcento do salário: R$%.2f' % trintaporcent_salario)
    print('Prestação mensal: R$%.2f' % prestacao_mensal)
    print('Prejuízo: R$%.2f' % (trintaporcent_salario - prestacao_mensal))
else:
    print('SUCESSO!')
    print()
    print('Valor do salário: R$%.2f' % salario)
    print('Valor do empréstimo: R$%.2f' % valor_casa)
    print('Tempo a pagar: ', tempo_pagar, 'meses')
    print('30 porcento do salário: R$%.2f' % trintaporcent_salario)
    print('Prestação mensal: R$%.2f' % prestacao_mensal)
    print('Limite: R$%.2f' % (trintaporcent_salario - prestacao_mensal))
