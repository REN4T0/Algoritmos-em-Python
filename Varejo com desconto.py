preco_original = float(input('Informe o preço original do produto: R$'))
desc = 0.2

print('Valor original: R$', preco_original)
print('Valor do desconto aplicado: R$', preco_original * desc)
print('Valor com desconto: R$%.2f' % (preco_original - (preco_original * desc)))
