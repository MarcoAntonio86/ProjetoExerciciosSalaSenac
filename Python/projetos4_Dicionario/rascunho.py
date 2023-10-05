'''Construa um programa para gerenciar um catálogo de produtos em uma loja. Os 
usuários podem adicionar produtos com informações como nome, preço e quantidade 
em estoque. Use um dicionário onde as chaves são os nomes dos produtos e os valores 
são outros dicionários com informações sobre cada produto.'''

import os
os.system('cls')

cadastro = {}

menu = ('Menu: \n'
    '1. Adicionar contato \n'
    '2. Remover contato \n'
    '3. Visualizar produtos \n'
    '4. Editar contato \n'
    '5. Sair \n')

print(menu)

escolha = 0

def exibir_contatos():
    if len(cadastro) == 0:
        print('O catalógo está vazio.')
    else:
        print('Catálogo:')
        for nome, detalhes in cadastro.items():
            print(f"Nome: {nome}, Produto: {detalhes['produto']}, preço {detalhes['preco']}, quantidade {detalhes['quantidade']}, estoque {detalhes['estoque']},")
        print()

def editar_contato():
    if len(cadastro) == 0:
        print('A agenda está vazia.')
    else:
        print('Contatos:')
        for nome, detalhes in cadastro.items():
             print(f"Nome: {nome}, Produto: {detalhes['produto']}, preço {detalhes['preco']}, quantidade {detalhes['quantidade']}, estoque {detalhes['estoque']},")        nome_editar = input('Informe o nome do contato que deseja editar: ')
        if nome_editar in cadastro:
            print(f'Editar contato: {nome_editar}')
            produto = input('Digite o novo produto: ')
            preco = input('Digite o novo preco: ')
            quantidade = input('Digite a nova quantidade: ')
            cadastro[nome_editar] = {'Produto': produto, 'preco': preco, 'quantidade': quantidade}
            print(f"O item '{nome_editar}' foi atualizado com sucesso!")
        else:
            print(f"O item '{nome_editar}' não existe no catalogo.")

while escolha != 5:
    escolha = int(input('Informe a opção: '))
    if escolha == 1:
        nome = input('Digite o nome do produto: ')
        preco = input('Digite o preço: ')
        quantidade = input('Digite a quantidade: ')
        con[nome] = {'telefone': telefone, 'email': email}
    elif escolha == 2:
        if len(contatos) == 0:
            print('Não há contatos para remover!')
        else:
            exibir_contatos()
            nome_remover = input('Informe o nome do contato que deseja remover: ')
            if nome_remover in contatos:
                del contatos[nome_remover]
                print(f"O contato '{nome_remover}' foi removido com sucesso!")
            else:
                print(f"O contato '{nome_remover}' não existe na agenda.")
    elif escolha == 3:
        exibir_contatos()
    elif escolha == 4:
        editar_contato()
    elif escolha == 5:
        print("Aplicativo encerrado.")
        break
    else:
        print('Opção inválida')