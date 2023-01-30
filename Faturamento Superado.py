faturamento_concorrente = 54000
lucro_final = 0
contador = 0

while(True):
    cliente = str(input('Informe o nome do cliente: '))
    valor_compra = float(input('Informe o valor da compra: '))
    print()

    while(valor_compra < 0):
        print('Valor de compra não correspondente!')
        valor_compra = float(input('Informe o valor da compra novamente: '))
        print()
        

    contador += 1
    lucro_final += valor_compra
    
    print('Para encerrar, digite 0!')
    continuar = int(input('Deseja continuar? - '))
    print()
    if(continuar == 0):
        break
if(lucro_final > faturamento_concorrente):
    print('O lucro superou o fauramento do concorrente!')
    print('Quantidade superada: R$%.2f' % (lucro_final - faturamento_concorrente))
    print('Número de clientes cadastrados: ', contador)
elif(lucro_final == faturamento_concorrente):
    print('O lucro alcançou o fauramento do concorrente!')
    print('Lucro final: R$%.2f' % lucro_final)
    print('Número de clientes cadastrados: ', contador)
else:
    print('Número de clientes cadastrados: ', contador)
    print('Valor total da compra dos clientes: R$%.2f' % lucro_final)
    print('Lucro restante para superar o faturamento do concorrente: R$%.2f' % (faturamento_concorrente - lucro_final))
