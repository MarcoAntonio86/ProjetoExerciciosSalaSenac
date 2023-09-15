lista = []
escolha = 0

menu = ('Menu: \n'
    '1. Adicionar tarefa \n'
    '2. Remover tarefa \n'
    '3. Listar tarefas pendentes \n'
    '4. Sair \n')

print(menu)

while escolha != 4:
    if escolha == 1:
        tarefa = input('Descreva a tarefa: ')
        lista.append(tarefa)
        print('Tarefa adicionada com sucesso !')
    elif escolha == 2:
        if len(lista) == 0:
            print('Não tem tarefas !')
        else:
            print(lista)
            tarefa_removida = input('Informe a tarefa que deseja remover: ')
            lista.remove(tarefa_removida)
            print(f"A tarefa '{tarefa_removida}' foi removida com sucesso!")
            print(lista)
    elif escolha == 3:
        if len(lista) == 0:
            print('Não tem tarefas pendentes.')
        else:
            print('Tarefas pendentes:')
            for i, tarefa in enumerate(lista):
                print(f"{i+1}. {tarefa}")
            print()
    elif escolha == 4:
        print("Aplicativo encerrado.")
        break