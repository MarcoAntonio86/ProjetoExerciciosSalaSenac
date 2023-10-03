

'''Dado um texto, conte quantas vezes cada caractere aparece (incluindo
espaços e caracteres especiais) e armazene os resultados em um
dicionário.'''


import os
os.system('cls')

texto = input("Digite o texto: ")

contagem_caracteres = {}  # Criar um dicionário vazio para armazenar a contagem

for caractere in texto:
    if caractere.isdigit():
        print("Erro: O texto não pode conter números.")
        break
    if caractere in contagem_caracteres:
        contagem_caracteres[caractere] += 1
    else:
        contagem_caracteres[caractere] = 1

# Imprimir a contagem de caracteres
for chave, valor in contagem_caracteres.items():
    print(f"'{chave}': {valor}")
