produtos = []
precos = []
quantidades = []
escolha = 0

menu = ('Menu: \n'
    '1. Adicionar produto o produto, preço e quantidade \n'
    '2. Remover produto, preço e quantidade \n'
    '3. Listas de produto, preço e quantidade cadastrado \n'
    '4. Sair \n')

print(menu)



while escolha != 4:
    escolha = int(input('Informe a opção: '))
    if escolha == 1:
        produto = input('informe o produto a ser cadastrado: ')
        preco = float(input('informe o preco do produto: '))
        quantidade = float(input('informe a quantidade do produto: '))
        produtos.append(produto)
        precos.append(preco)
        quantidades.append(quantidade)

    elif escolha == 2:
        if len(produtos) == 0:
            print('Não tem produto a ser removido do cadastro !')
        else:
            print(produtos)
            produto_removido = input('Informe o produto que deseja remover: ')
            produtos.remove(produto_removido)
            precos.remove(produto_removido)
            quantidades.remove(produto_removido)
            print(f"O produto '{produto_removido}' foi removido com sucesso!")
            print(produtos)
            print(precos)
            print(quantidades)
    elif escolha == 3:
        if len(produtos) == 0:
            print('Não tem produto cadastro !')
        else:
            print('Produtos cadastrados:')
            for i, produto in enumerate(produtos):
                tupla_produto = (produtos)
                print(f"{i+1}. {tupla_produto}")
            print()
            for j, preco in enumerate(precos):
                tupla_preco = (precos)
                print(f"{j+1}. {preco}")
            print()
            for k, quantidade in enumerate(quantidades):
                tupla_quantidade = (quantidades)
                print(f"{k+1}. {quantidade}")
            print()
    elif escolha == 4:
        print("Aplicativo encerrado.")
        break
    else:
        print('Opção invalida')

    
  
        

