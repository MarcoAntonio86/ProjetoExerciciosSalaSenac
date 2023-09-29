''' : Contagem de Palavras com Lista de Frases
        Dado um dicionário de informações de alunos, escreva um programa que
        filtre os alunos que têm uma nota superior a 85 e crie um novo dicionário
         com esses alunos.'''





cadastro = {
    "nomes": [],
    "notas1": [],
    "notas2": [],
    "notas3": [],
    "notas4": [],
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
x = zip(cadastro['nomes'], cadastro['notas1'], cadastro['notas2'], cadastro['notas3'], cadastro['notas4'])
print(x)