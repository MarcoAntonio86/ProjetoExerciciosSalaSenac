tarefas = []

while True:
   
    print("Menu:")
    print("1. Adicionar tarefa")
    print("2. Remover tarefa")
    print("3. Listar tarefas pendentes")
    print("4. Sair")

    escolha = input("Digite o número correspondente à opção desejada: ")

    if escolha == "1":
        tarefa = input("Digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        print("Tarefa adicionada com sucesso!")
        print()

    elif escolha == "2":
        if len(tarefas) == 0:
            print("Não há tarefas para remover.")
            print()
        else:
            print("Tarefas pendentes:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1}. {tarefa}")
            indice = int(input("Digite o número correspondente à tarefa que deseja remover: ")) - 1
            if indice < 0 or indice >= len(tarefas):
                print("Índice inválido.")
                print()
            else:
                tarefa_removida = tarefas.pop(indice)
                print(f"A tarefa '{tarefa_removida}' foi removida com sucesso!")
                print()

    elif escolha == "3":
        if len(tarefas) == 0:
            print("Não há tarefas pendentes.")
            print()
        else:
            print("Tarefas pendentes:")
            for i, tarefa in enumerate(tarefas):
                print(f"{i+1}. {tarefa}")
            print()

    elif escolha == "4":
        print("Aplicativo encerrado.")
        break

    else:
        print("Opção inválida. Digite o número correspondente à opção desejada.")
        print()