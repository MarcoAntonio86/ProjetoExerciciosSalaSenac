import os
os.system('cls')

import statistics

cadastro = {
    "nomes": [],
    "nota": [],
}

aprovados = []


while True:

    nomes = input("Digite o nome do aluno: ")
    cadastro['nomes'].append(nomes)
    nota = input("Digite a nota: ")
    if nota.isdigit():
            nota = float(nota)
            cadastro['nota'].append(nota)
    else:
            print('Valor inválido. Por favor, informe um número inteiro.')
    pergunta = input("Deseja adicionar mais um aluno? [S/N] ").strip().upper()
    if pergunta == 'N':
        break

for nome, notas in zip(cadastro['nomes'], cadastro['nota']):
       if notas >= 85:
          aprovados.append(nome)
print("Alunos aprovados:", aprovados)
