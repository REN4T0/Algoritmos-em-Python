salario = float(input('Digite o valor equivalente ao salário: R$'))
desc_imposto = 0.125

if (salario < 2200):
    print('Salário abaixo do requerido. Não há necessidade de pagar imposto.')
else:
    imposto = salario * desc_imposto
    print('Salário informado: R$%.2f' % salario)
    print('Valor do imposto: R$%.2f' % imposto)
    print('Salário líquido: R$%.2f' % (salario - imposto))
