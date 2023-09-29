print('Controle de pescado !')
pescados = float(input('informe a quantidade de Kilo pescado: '))
multa = (pescados - 50)*4
if pescados <= 50:
    print('Você atingiu a sua cota de pesca, não há multa !')
else:
   
    print('O valor da multa será de R$ {:.2f}' .format(multa))


