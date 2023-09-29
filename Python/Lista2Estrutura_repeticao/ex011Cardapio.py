
total = 0
total_itens = 0
print ('------Menu------ \n'
       'o Especificação Código Preço \n'
       'o Cachorro Quente 100 R$ 1,20 \n'
       'o Bauru Simples 101 R$ 1,30 \n'
       'o Bauru com ovo 102 R$ 1,50 \n'
       'o Hambúrguer 103 R$ 1,20 \n'
       'o Cheeseburguer 104 R$ 1,30 \n'
       'o Refrigerante 105 R$ 1,00 \n'
       '\n'
)

while True:
    codigo = input('Informe o código do produto: ')
    quantidade = float(input('Informe a quantidade: '))
    if codigo == '100':
        preco = 1.20
        total = preco * quantidade
        total_itens += total
        
        print(f'O valor a ser pago, do produto {codigo} é de R$ {total:.2f}')
    elif codigo == '101':
        preco = 1.30
        total = preco * quantidade
        total_itens += total
        
        print(f'O valor a ser pago, do produto {codigo} é de R$ {total:.2f}')
    elif codigo == '102':
        preco = 1.50
        total = preco * quantidade
        total_itens += total
        print(f'O valor a ser pago, do produto {codigo} é de R$ {total:.2f}')
    elif codigo == '103':
        preco = 1.20
        total = preco * quantidade
        total_itens += total
        
        print(f'O valor a ser pago, do produto {codigo} é de R$ {total:.2f}')
    elif codigo == '104':
        preco = 1.30
        total = preco * quantidade
        total_itens += total
        
        print(f'O valor a ser pago, do produto {codigo} é de R$ {total:.2f}')
    elif codigo == '105':
        preco = 1.00
        total = preco * quantidade
        total_itens += total
        
        print(f'O valor a ser pago, do produto {codigo} é de R$ {total:.2f}')
    else:
        print('Produto inexistente')
        continue
    
    
    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        print(f'Total gasto: R$ {total_itens:.2f}')
        break

    print(f'Total gasto: R$ {total_itens:.2f}')

    

   
