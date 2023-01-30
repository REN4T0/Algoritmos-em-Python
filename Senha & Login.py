usuario = ('renato')
password = ('password')
i = 0

login = str(input('Login: '))    
senha = str(input('Senha: '))
print()

while(login != usuario)or(senha != password):
    print('Login e/ou senha incorretos! Digite novamente...')
    print()

    i += 1
    
    login = str(input('Login: '))    
    senha = str(input('Senha: '))
    print()

    if(i == 5):
        break

if(i == 5):
    print('Ocorreu um erro inesperado! Tente novamente mais tarde.')
else:
    print('Acesso liberado!')



