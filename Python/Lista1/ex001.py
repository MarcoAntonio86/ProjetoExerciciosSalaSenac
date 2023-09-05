print('Controle de pescado !')
pescados = float(input('informe a quantidade de Kilo pescado: '))

if pescados <= 50:
    print('Você atingiu a sua cota de pesca, não há multa !')
else:
    multa = pescados - 50
    print('O valor da multa será de R$ ' + multa)


