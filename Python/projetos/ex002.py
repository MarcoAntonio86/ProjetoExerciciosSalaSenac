tarefas = []

menu = ('Menu: \n'
    '1. Adicionar tarefa \n'
    '2. Remover tarefa \n'
    '3. Listar tarefas pendentes \n'
    '4. Sair \n')

while True:

    print(menu)

    escolha = input('Digite o número correspondente à opção desejada: ')

    if escolha == '1':
        tarefa = input('Descreva a tarefa: ')
        tarefas.append(tarefa)
        print('Tarefa adicionada com sucesso !')
    
    elif escolha == '2':
        if len(tarefas) == 0:
            print('Não tem tarefas !')
        
        else:
            print('Aqui ')

