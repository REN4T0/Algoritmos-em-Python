# Prêmio a ser dividido
total = float(input('Informe o valor total do prêmio: '))

# Número de ganhadores
num = int(input('Informe o número de ganhadores: '))

# Mostrar o valor de cada ganhador e fazer a operação do cálculo
print('Cada ganhador receberá o valor de R$%.2f' % (total / num))
