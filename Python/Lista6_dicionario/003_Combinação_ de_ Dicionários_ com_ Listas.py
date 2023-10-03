'''Crie um programa que combine dicionários com informações de alunos,
incluindo nome, idade e notas. Os dados estão armazenados em listas
separadas.'''


import os
os.system('cls')

cadastro = {
    "nomes": [],
    "idade": [],
    "notas": [],
}

def get_nomes():
    nomes = input("Digite o nome do aluno: ")
    cadastro['nomes'].append(nomes)

def get_idade():
    idade = input("Digite a idade do aluno: ")
    if idade.isdigit():
        idade = int(idade)
        cadastro['idade'].append(idade)
    else:
        print('Valor inválido. Por favor, informe um número inteiro.')


def get_nota():
        nota = input("Digite a nota: ")
        if nota.isdigit():
            nota = float(nota)
            cadastro['notas'].append(nota)
        else:
            print('Valor inválido. Por favor, informe um número inteiro.')
            

while True:
    get_nomes()
    get_idade()
    get_nota()
    pergunta = input("Deseja adicionar mais um aluno? [S/N] ").strip().upper()
    if pergunta == 'N':
        break


for nome, idade, nota in zip(cadastro['nomes'], cadastro['idade'], cadastro['notas']):
    print(f'Nome do aluno: {nome}, \n sua idade: {idade}, \n suas nota: {nota}')