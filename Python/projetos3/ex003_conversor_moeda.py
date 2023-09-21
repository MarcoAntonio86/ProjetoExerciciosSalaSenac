
moeda = 0
cotacao = 0
resultado = 0
def valor_moeda_maior (moeda, cotacao):
    return moeda * cotacao
   

def valor_moeda_menor (moeda, cotacao):
    return moeda / cotacao
    

def moeda_que_tenho (informa):
    print(informa)

def moeda_que_quero (informa2):
    print(informa2)


while True:
    informa = input('Informe a moeda que quer converter:  ')
    informa2 = input('Para qual moeda deseja converter:  ')
    
    moeda = float(input('informe a quantidade de moeda que quer converter:  '))
    cotacao = float(input('informe a cotação da moeda:  '))
    
    sinal = input('Informe, com os sinais < e >, se a cotação é a maior ou a menor em relação a moeda informada : ')

    if sinal == '<':
        resultado = valor_moeda_maior(moeda, cotacao)
    elif sinal == '>':
        resultado = valor_moeda_menor(moeda, cotacao)

    print(f'A cotação de {informa} em {informa2} é de {resultado:.2f}')

    pergunta = input('Deseja continuar? [S/N] ').strip().upper()
    if pergunta == 'N':
        break

print('Programa encerrado.')
    

