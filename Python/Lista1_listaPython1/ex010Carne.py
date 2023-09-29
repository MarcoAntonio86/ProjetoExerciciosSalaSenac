carne = input('Informe o tipo de carne, se File Duplo use F, se Alcatra use A e se Picanha use P: ').strip().upper()
kilo = float(input('Informe a quantidade de carne: '))
pagto = input('Informe o tipo de pagamento, se Dinheiro use D e se Cartão use C: ').strip().upper()
file_preco1 = 4.90
file_preco2 = 5.80
Alcatra_preco1 = 5.90
Alcatra_preco2 = 6.80
Picanha_preco1 = 6.90
Picanha_preco2 = 7.80
resultado = 0

if carne == 'F':
    if kilo <= 5:
        resultado = file_preco1 * kilo
    else:
        resultado = file_preco2 * kilo
elif carne == 'A':
    if kilo <= 5:
        resultado = Alcatra_preco1 * kilo
    else:
        resultado = Alcatra_preco2 * kilo
elif carne == 'P':
    if kilo <= 5:
        resultado = Picanha_preco1 * kilo
    else:
        resultado = Picanha_preco2 * kilo

print('O valor a ser pago é de R$ {:.2f}'.format(resultado))

if pagto == 'C':
    resultado = resultado - (resultado * 0.10)
    print('O valor a ser pago, com o desconto pelo uso do cartão, é de R$ {:.2f}'.format(resultado))
else:
    print('Sem desconto')