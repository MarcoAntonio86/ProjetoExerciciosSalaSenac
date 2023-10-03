'''Modifique o exercício anterior para criar um dicionário de dicionários, 
onde cada aluno é representado por um dicionário contendo idade e 
nota.'''

import os
os.system('cls')



nomes = {
    'alunos': [],
}

cadastro = {
    'idades': [],
    'notas': [],
}

def get_nomes():
    nome = input("Digite o nome do aluno: ")
    nomes['alunos'].append(nome)

def get_idade():
    while True:
        idade = input("Digite a idade do aluno: ")
        if idade.isdigit():
            idade = int(idade)
            cadastro['idades'].append(idade)
            break  
        else:
            print('Valor inválido. Por favor, informe um número inteiro.')



def get_nota():
    
     while True:
        nota = input("Digite a nota: ")
        try:
            nota = float(nota)
            cadastro['notas'].append(nota)
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

    
    
print(f'Nome do aluno: {nomes}')
print(f'Idade e nota do aluno: {cadastro}')

nomes.update(cadastro)

print(cadastro)