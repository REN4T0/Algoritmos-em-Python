print('MEDIDAS DE SEGURANÇA')
print('Limite de pessoas no elevador - 30')
print('Limite de peso no elevador - 2100kg')

print()

alunos = int(input('Informe a quantidade de alunos: '))

monitores = int(input('Informe a quantidade de monitores: '))

print()

peso_limite = 2100
quantidade_limite = 30

if((alunos + monitores) > quantidade_limite):
	sobra = (alunos + monitores) - quantidade_limite
	print((alunos + monitores), 'Pessoas')
	print('Quantidade acima do limite de segurança! Terão que sair', sobra, 'do elevador.')
	
	print()
	
	i = 0
	kgtotal = 0
	while(i < ((alunos + monitores) - sobra)):
		i += 1
		
		peso = float(input('Digite o peso: '))
		
		kgtotal += peso
		
		if(kgtotal > peso_limite):
			break
	
	print()
	
	if(kgtotal > peso_limite):
		print(kgtotal, 'kg')
		print('NNN - Peso acima do limite')
	else:
		print('Quantidade de pessoas:', ((alunos + monitores) - sobra))
		print('Peso total:', kgtotal)
		
elif((alunos + monitores) < 1):
		print('ERRO! Número impossível ou nulo de pessoas.')
		
else:
	i = 0
	kgtotal_aluno = 0
	kgtotal_monitor = 0
	kgtotal = 0
	
	while(i < alunos):
		i += 1
		
		peso_aluno = float(input('Digite o peso do aluno: '))
		
		kgtotal_aluno += peso_aluno
	
	print()
		
	restante = peso_limite - kgtotal_aluno
	print('Peso preenchido:', kgtotal_aluno, 'kg')
	print('Peso limite restante:', restante, 'kg')
	
	print()
	
	i = 0
	
	while(i < monitores):
		i += 1
		
		peso_monitor = float(input('Digite o peso do monitor: '))
		
		kgtotal_monitor += peso_monitor
		
	kgtotal = kgtotal_aluno + kgtotal_monitor
	
	print()
	
	if(kgtotal > peso_limite):
		print(kgtotal, 'kg')
		print('NNN - Peso acima do limite')
	else:
		print('Quantidade de pessoas:', (alunos + monitores))
		print('Peso total:', kgtotal, 'kg')
		print('Acesso Liberado!')
