''' : Contagem de Palavras com Lista de Frases
        Dado um dicionário de informações de alunos, escreva um programa que
        filtre os alunos que têm uma nota superior a 85 e crie um novo dicionário
         com esses alunos.'''


import os
os.system('cls')

import statistics

cadastro = {
    "nomes": [],
    "notas1": [],
    "notas2": [],
    "notas3": [],
    "notas4": [],
}

estatus = {
    "aprovado": [],
    "reprovado": [],
}

while True:

 nomes = input("Digite o nome do aluno: ")
 cadastro['nomes'].append(nomes)
 notas1 = float(input("Digite a primeira nota: "))
 cadastro['notas1'].append(notas1)
 notas2 = float(input("Digite a segunda nota: "))
 cadastro['notas2'].append(notas2)
 notas3 = float(input("Digite a terceira nota: "))
 cadastro['notas3'].append(notas3)
 notas4 = float(input("Digite a quarta nota: "))
 cadastro['notas4'].append(notas4)
 pergunta = input("Deseja adicionar mais um aluno? [S/N] ").strip().upper()
 if pergunta == 'N':    
     break
 

print(cadastro)
for nome, nota1, nota2, nota3, nota4 in zip(cadastro['nomes'], cadastro['notas1'], cadastro['notas2'], cadastro['notas3'], cadastro['notas4']):
    print(f'nomes: {nome}, nota 1: {nota1}, nota 2: {nota2}, nota 3: {nota3}, nota 4: {nota4}')

print("Média de cada aluno:")
for nome, nota1, nota2, nota3, nota4 in zip(cadastro['nomes'], cadastro['notas1'], cadastro['notas2'], cadastro['notas3'], cadastro['notas4']):
    notas_aluno = [nota1, nota2, nota3, nota4]
    media_aluno = statistics.mean(notas_aluno)
    print(f'Nome: {nome}, Média: {media_aluno}')

todasnotas = cadastro['notas1'] + cadastro['notas2'] + cadastro['notas3'] + cadastro['notas4']
media = statistics.mean(todasnotas)

print(f'Média geral de todas as notas: {media}')

if media_aluno >= 85:
    for status in nome:
        print(f'Aluno(a) {nome} foi aprovado(a)')
else:
    for status in nome:
        print(f'Aluno(a) {nome} foi reprovado(a)')
    



