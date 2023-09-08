fruta = input('Informe se é Morango ou Maçã: ').strip().upper()
peso = float(input('Informe o peso: '))
Mor_preco1 = 2.50
Mor_preco2 = 2.20
Mac_preco1 = 1.80
Mac_preco2 = 1.50
resultado = 0

if fruta == 'MORANGO':
    if peso <= 5:
        resultado = Mor_preco1 * peso
    else:
        resultado = Mor_preco2 * peso
elif fruta == 'MAÇÃ':
    if peso <= 5:
        resultado = Mac_preco1 * peso
    else:
        resultado = Mac_preco2 * peso
if peso >= 8 and resultado >= 25:
    resultado = resultado - (resultado * 0.10)    

print('O valor a ser pago é de R$ {:.2f}'.format(resultado))

