
livros_disponiveis = (
    ("Dom Casmurro", "Machado de Assis", 25.00, 50),
    ("A Moreninha", "Joaquim Manuel de Macedo", 20.00, 30),
    ("Memórias Póstumas de Brás Cubas", "Machado de Assis", 30.00, 40),
)


escolha = 0

menu = ('Menu: \n'
    '1. Adicionar livro \n'
    '2. Remover livro \n'
    '3. Atualizar informações do livro \n'
    '4. Listar livros disponíveis \n'
    '5. Sair \n')

print(menu)

while escolha != 5:
    escolha = int(input('Informe a opção: '))

    if escolha == 1:
        titulo = input('Informe o título do livro: ')
        autor = input('Informe o autor do livro: ')
        preco = float(input('Informe o preço do livro: '))
        quantidade = int(input('Informe a quantidade em estoque: '))
        livro_novo = (titulo, autor, preco, quantidade)
        livros_disponiveis += (livro_novo,)
        print(f'O livro "{titulo}" foi adicionado ao estoque.')

    elif escolha == 2:
        titulo = input('Informe o título do livro a ser removido: ')
        livro_encontrado = None
        for livro in livros_disponiveis:
            if livro[0] == titulo:
                livro_encontrado = livro
                break

        if livro_encontrado:
            livros_disponiveis = tuple(l for l in livros_disponiveis if l != livro_encontrado)
            print(f'O livro "{titulo}" foi removido do estoque.')
        else:
            print(f'O livro "{titulo}" não encontrado no estoque.')

    elif escolha == 3:
        titulo = input('Informe o título do livro a ser atualizado: ')
        livro_encontrado = None
        for i, livro in enumerate(livros_disponiveis):
            if livro[0] == titulo:
                preco = float(input('Informe o novo preço do livro: '))
                quantidade = int(input('Informe a nova quantidade em estoque: '))
                livro_novo = (titulo, livro[1], preco, quantidade)
                livros_disponiveis = livros_disponiveis[:i] + (livro_novo,) + livros_disponiveis[i+1:]
                print(f'As informações do livro "{titulo}" foram atualizadas.')
                break
        else:
            print(f'O livro "{titulo}" não encontrado no estoque.')

    elif escolha == 4:
        if len(livros_disponiveis) == 0:
            print('Não há livros disponíveis!')
        else:
            print('Livros disponíveis:')
            for livro in livros_disponiveis:
                titulo, autor, preco, quantidade = livro
                print(f'Título: {titulo}, Autor: {autor}, Preço: R${preco:.2f}, Estoque: {quantidade}')

    elif escolha == 5:
        print("Aplicativo encerrado.")
        break

    else:
        print('Opção inválida')
