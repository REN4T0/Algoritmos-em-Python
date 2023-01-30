preco_produto = float(input('Digite o valor do produto: R$'))
desc = float(input('Digite o valor do desconto em porcento(%): '))

print('Valor original do produto: R$%.2f' % preco_produto)
print('Valor do desconto: R$%.2f' % (preco_produto * (desc / 100)))
print('Valor final do produto com desconto: R$%.2f' % (preco_produto - (preco_produto * (desc / 100))))
