combustivel = str(input('Qual o tipo de combustível você deseja? - '))
litro = float(input('Digite a quantidade de litros a abastecer: '))

preco_gasolina = 4.89
preco_alcool = 3.78

desconto_gasolina1 = (preco_gasolina * litro) * 0.04
desconto_gasolina2 = (preco_gasolina * litro) * 0.06

desconto_alcool1 = (preco_alcool * litro) * 0.03
desconto_alcool2 = (preco_alcool * litro) * 0.05

if(combustivel == 'G')and(combustivel == 'g'):
    if(litro < 21)and(litro > 0):
        preco_pagar = (preco_gasolina * litro) - desconto_gasolina1
    elif(litro > 20):
        preco_pagar = (preco_gasolina * litro) - desconto_gasolina2
    else:
        print('erro')
    print(preco_pagar)

elif(combustivel == 'A')and(combustivel == 'a'):
    if(litro < 21)and(litro > 0):
        preco_pagar = (preco_alcool * litro) - desconto_alcool1
    elif(litro > 20):
        preco_pagar = (preco_alcool * litro) - desconto_alcool2
    else:
        print('erro')
else:
    print('erro')

print(preco_pagar)

