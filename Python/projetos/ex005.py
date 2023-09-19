lista = []
escolha = 0

menu = ('Menu: \n'
    '1. Adicionar produto ao carrinho \n'
    '2. Remover produto do carrinho \n'
    '3. Listas de produto no carrinho \n'
    '4. Sair \n')

print(menu)



while escolha != 4:
    escolha = int(input('Informe a opção: '))
    if escolha == 1:
        produto = input('informe o produto a ser cadastrado: ')
        lista.append(produto)
        print('Produto adicionado com sucesso !')
    elif escolha == 2:
        if len(lista) == 0:
            print('Não tem produto a ser removido do carrinho !')
        else:
            print(lista)
            produto_removido = input('Informe o produto que deseja remover: ')
            lista.remove(produto_removido)
            print(f"O produto '{produto_removido}' foi removido com sucesso!")
            print(lista)
    elif escolha == 3:
        if len(lista) == 0:
            print('Não tem produtos cadastrado.')
        else:
            print('Produtos cadastrado:')
            for i, produto in enumerate(lista):
                print(f"{i+1}. {produto}")
            print()
    elif escolha == 4:
        print("Aplicativo encerrado.")
        break
    else:
        print('Opção invalida')
        