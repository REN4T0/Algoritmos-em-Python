login = str(input('Login: '))
senha = str(input('Senha: '))
print()

while(senha == login):
	print('A senha não deve ser igual ao login! Digite outra senha.')
	print()
	senha = str(input('Senha: '))
	print()

print('Acesso: Liberado')
