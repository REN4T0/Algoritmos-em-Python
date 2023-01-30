kwh = float(input('Informe a quantidade de quilowatt consumido por hora: '))
print()

print('TIPOS DE INSTALAÇÃO')
print('R - Residencial')
print('C - Comercial')
print('I - Industrial')
print()

instalacao = str(input('Informe o tipo de instalação: '))

print()

preco_residencia1 = 40
preco_residencia2 = 65

preco_comercio1 = 55
preco_comercio2 = 60

preco_industria1 = 59
preco_industria2 = 72

if(instalacao == 'r')or(instalacao == 'R'):
    if(kwh < 501):
        imposto = kwh * preco_residencia1
        print()
        print('Quilowatt consumido por hora: ', kwh)
        print('Valor a ser aplicado sobre o consumo: R$%.2f' % preco_residencia1)
    else:
        imposto = kwh * preco_residencia2
        print()
        print('Quilowatt consumido por hora: ', kwh)
        print('Valor a ser aplicado sobre o consumo: R$%.2f' % preco_residencia2)
elif(instalacao == 'c')or(instalacao == 'C'):
    if(kwh < 1001):
        imposto = kwh * preco_comercio1
        print()
        print('Quilowatt consumido por hora: ', kwh)
        print('Valor a ser aplicado sobre o consumo: R$%.2f' % preco_comercio1)
    else:
        imposto = kwh * preco_comercio2
        print()
        print('Quilowatt consumido por hora: ', kwh)
        print('Valor a ser aplicado sobre o consumo: R$%.2f' % preco_comercio2)
elif(instalacao == 'i')or(instalacao == 'I'):
    if(kwh < 5001):
        imposto = kwh * preco_industria1
        print()
        print('Quilowatt consumido por hora: ', kwh)
        print('Valor a ser aplicado sobre o consumo: R$%.2f' % preco_industria1)
    else:
        imposto = kwh * preco_industria2
        print()
        print('Quilowatt consumido por hora: ', kwh)
        print('Valor a ser aplicado sobre o consumo: R$%.2f' % preco_industria2)
else:
    print('Instalação desconhecida no sistema.')

print('Imposto a pagar: R$%.2f' % imposto)
