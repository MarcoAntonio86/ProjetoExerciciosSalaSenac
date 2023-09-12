print ('------Menu------'
       'o Especificação Código Preço'
       'o Cachorro Quente 100 R$ 1,20'
       'o Bauru Simples 101 R$ 1,30'
       'o Bauru com ovo 102 R$ 1,50'
       'o Hambúrguer 103 R$ 1,20'
       'o Cheeseburguer 104 R$ 1,30'
       'o Refrigerante 105 R$ 1,00'
       '\n'
)

while True:
    codigo = input('Informe o código do produto: ')
    quantidade = float(input('Informe a quantidade: '))
    if codigo == '100':
        preco = 1.20
    elif codigo == '101':
        preco = 1.30
    elif codigo == '102':
        preco = 1.50
    elif codigo == '103':
        preco = 1.20
    elif codigo == '104':
        preco = 1.30
    elif codigo == '105':
        preco = 1.00
    else:
        print('Produto inexistente')
        continue
    total = preco * quantidade
    print(f'O valor a ser pago, do produto {codigo} é de R$ {total:.2f}')
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

    # FAZER MODIFICAÇÕES, COLOCAR UM TOTAL PRINTADO EM TODOS OS IFS
