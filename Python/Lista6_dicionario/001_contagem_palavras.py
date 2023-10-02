''' : Contagem de Palavras com Lista de Frases
        Dado um dicionário de informações de alunos, escreva um programa que
        filtre os alunos que têm uma nota superior a 85 e crie um novo dicionário
         com esses alunos.'''
import os
os.system('cls')

import statistics

cadastro = {
    "nomes": [],
    "nota": [],
}

aprovados = []


def get_nomes():
    nomes = input("Digite o nome do aluno: ")
    cadastro['nomes'].append(nomes)
def get_nota():
    
        nota = input("Digite a nota: ")
        if nota.isdigit():
            nota = float(nota)
            cadastro['nota'].append(nota)
        else:
            print('Valor inválido. Por favor, informe um número inteiro.')

            return nota
        



'''def aprova():
    if nota >= 85:
        aprovados.append(nomes)
        print(aprovados)
    return aprovados'''

def aprova():
    notas_alunos = cadastro['notas']
    for nome, nota in zip(cadastro['nomes'], notas_alunos):
        if nota >= 85:
            aprovados.append(nome)
    print("Alunos aprovados:", aprovados)
    return aprovados





while True:
   get_nomes()
   get_nota()
   pergunta = input("Deseja adicionar mais um aluno? [S/N] ").strip().upper()
   if pergunta == 'N':    
        break
    
aprova()
    
