print('Digite 0 para encerrar o processo!')
print()

num = int
soma = 0

while(num != 0):
	num = int(input('Digite um número inteiro: '))
	
	soma += num

print()
print('Soma dos valores digitados: ', soma)