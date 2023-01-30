def fatorial(numero):
    resultado = 1
    if(numero == 0)or(numero == 1):
        resultado = 1
    else:
        while(numero >= 1):
            resultado = resultado * numero
            numero -= 1
        
    return resultado
