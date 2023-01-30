print('CÁLCULO DE GRANDEZAS ELÉTRICAS')
print()

print('1. Tensão------(Volts)')
print('2. Resistência-(Ohm)')
print('3. Corrente----(Ampére)')
print()


grandeza = int(input('Qual grandeza deseja calcular? - '))
print()

tensao = 0
resistencia = 0
corrente = 0

if(grandeza == 1):
    resistencia = float(input('Informe a resistência: '))
    corrente = float(input('Informe a corrente elétrica: '))
    print()

    tensao = resistencia * corrente

    print('Tensão elétrica calculada:', tensao, 'V')
    
elif(grandeza == 2):
    tensao = float(input('Informe a tensão elétrica: '))
    corrente = float(input('Informe a corrente elétrica: '))
    print()

    resistencia = tensao / corrente

    print('Resistência elétrica calculada: ', resistencia, 'Ω')

elif(grandeza == 3):
    tensao = float(input('Informe a tensão elétrica: '))
    resistencia = float(input('Informe a resistência: '))
    print()

    corrente = tensao / resistencia

    print('corrente elétrica calculada:', corrente, ('A'))
else:
    print('ERRO - Valor irreconhecível')
