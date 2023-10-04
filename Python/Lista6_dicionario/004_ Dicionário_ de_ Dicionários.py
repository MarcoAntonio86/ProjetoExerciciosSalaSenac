'''Modifique o exercício anterior para criar um dicionário de dicionários, 
onde cada aluno é representado por um dicionário contendo idade e 
nota.'''

import os
os.system('cls')



alunos = {}

def get_aluno():
    nome = input("Digite o nome do aluno: ")

    while True:
        idade = input("Digite a idade do aluno: ")
        try:
            idade = int(idade)
            break
        except ValueError:
            print('Valor inválido. Por favor, informe um número.')

    while True:
        nota = input("Digite a nota do aluno: ")
        try:
            nota = float(nota)
            break
        except ValueError:
            print('Valor inválido. Por favor, informe um número.')

    aluno = {
        'nome': nome,
        'idade': idade,
        'nota': nota
    }

    return aluno

while True:
    aluno = get_aluno()
    alunos[aluno['nome']] = aluno  # Usando o nome como chave do dicionário
    pergunta = input("Deseja adicionar mais um aluno? [S/N] ").strip().upper()
    if pergunta != 'S':
        break

print("O cadastro ficou:")
for nome, dados in alunos.items():
    print(f'Nome: {dados["nome"]}, Idade: {dados["idade"]}, Nota: {dados["nota"]}')
