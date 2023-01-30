print('Para encerrar, digite 0.')
print()

preco = float
preco_final = 0
conceder_desconto = 1100


while(preco != 0):
	preco = float(input('Digite o preço: R$ '))
	
	while(preco <= -1):
		preco = float(input('O valor não pode ser negativo! Digite novamente: R$ '))
	
	preco_final += preco

if(preco_final >= conceder_desconto):
        desconto = preco_final * 0.15
        preco_final_desconto = preco_final - desconto

        print()
        print('Valor a pagar: R$%.2f' % preco_final_desconto)
else:
        print()
        print('Valor a pagar: R$%.2f' % preco_final)
