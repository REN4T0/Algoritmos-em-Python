base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

contador = 0
resultado = 1

while(contador < expoente):
    resultado *= base
    contador += 1

print(base,'elevado a',expoente,'é igual a',resultado)
