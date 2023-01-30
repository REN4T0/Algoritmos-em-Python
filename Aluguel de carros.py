i = 0

print('Olá! Bem-vindo ao serviço virtual de cobrança da Localiza!')
print()

print('Antes de informar os dados requeridos, siga as seguintes instruções...')
print()

print('- Consulte a quilometragem percorrida no carro em que você alugou. Ela está localizada diretamente no painel do veículo.')
print('Não se preocupe! Após o fim do aluguel, a quilometragem é zerada. Então você não vai pagar a mais pelos quilômetros que rodou.')
print()

print('- Para saber por quantos dias o veículo está com você, consulte o documento que deixamos com você no início do aluguel.')
print()

km = float(input('Quantos quilômetros você percorreu com o carro? - '))
dia = int(input('Por quantos dias o carro ficou com você? - '))

preco_perkm = 8.50
preco_perdia = 320

precofinal_km = km * preco_perkm
precofinal_dia = dia * preco_perdia
total_pagar = precofinal_km + precofinal_dia

print()

print('NOTA FISCAL')
print('Preço final por quilômetro(km): %.2f' % precofinal_km)
print('Preço final por dia: %.2f' % precofinal_dia)
print('Total a pagar: %.2f' % total_pagar)
