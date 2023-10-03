'''Crie um programa que combine dicionários com informações de alunos,
incluindo nome, idade e notas. Os dados estão armazenados em listas
separadas.'''


import os
os.system('cls')

alunos = {'alunos': []}
idades = {'idades': []}
notas = {'notas': []}
cadastro = {}

def get_nomes():
    nomes = input("Digite o nome do aluno: ")
    alunos['alunos'].append(nomes)

def get_idade():
    while True:
        idade = input("Digite a idade do aluno: ")
        if idade.isdigit():
            idade = int(idade)
            idades['idades'].append(idade)
            break  
        else:
            print('Valor inválido. Por favor, informe um número inteiro.')



def get_nota():
    while True:
        nota = input("Digite a nota: ")
        try:
            nota = float(nota)
            notas['notas'].append(nota)
            break
        except ValueError:
            print('Valor inválido. Por favor, informe um número.')
            

while True:
    get_nomes()
    get_idade()
    get_nota()
    pergunta = input("Deseja adicionar mais um aluno? [S/N] ").strip().upper()
    if pergunta == 'N':
        break


'''for nome, idade, nota in zip(cadastro['nomes'], cadastro['idade'], cadastro['notas']):
    print(f'Nome do aluno: {nome}, \n sua idade: {idade}, \n suas nota: {nota}')'''

print(f'Alunos: {alunos}')
print(f'Idades: {idades}')
print(f'Notas: {notas}')

cadastro.update(alunos)
cadastro.update(idades)
cadastro.update(notas)

print(cadastro)