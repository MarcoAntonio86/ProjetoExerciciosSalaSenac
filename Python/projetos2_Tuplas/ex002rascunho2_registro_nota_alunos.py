alunos = []
notas = []
medias = []
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
          nome_aluno = input('Informe o nome do aluno: ')
          nota1 = float(input('Informe a primeria nota: '))
          nota2 = float(input('Informe a segunda nota:'))
          nota3 = float(input('Informe a terceira nota:'))
          nota4 = float(input('Informe a quarta nota:'))
          media = (nota1 + nota2 + nota3 + nota4)/4
          alunos.append(nome_aluno)
          notas.append(nota1, nota2, nota3, nota4)
          medias.append(media)
          print('Aluno cadastrado com sucesso !')
          
     elif escolha == 2:
          if len(alunos):
               print('Não tem alunos cadastrado !')
          
          else:
               print(f'Os alunos são {alunos}')
               print(f'As notas são {nota1, nota2, nota3, nota4}')
               print(f'As medias são {medias}')
               alunos_removidos = input('Informe o nome do aluno a ser removido')
               alunos.remove(alunos_removidos)
               notas_removidas = float(input('Informe a nota a ser removida: '))
               notas.remove(notas_removidas)
               medias_removidas = float(input('Informe a média que se quer retirar: '))
               medias.remove(medias_removidas)
               print(f'O aluno a ser removido é {alunos_removidos}')
               print(f'As notas retiradas seram {notas_removidas}')
               print(f'A média retirada será {medias_removidas}')
               print(alunos)
               print(notas)
               print(medias)
     
     elif escolha == 3:
          if len(alunos):
               print('Não há alunos cadastrado !')
          
          else: 
               print('Alunos e notas cadastradas') 
               for cont_aluno, nome_aluno in enumerate(alunos):
                    print(f"{cont_aluno + 1}. {nome_aluno}. {nota1, nota2, nota3, nota4}. {media}")