

'''Dado um texto, conte quantas vezes cada caractere aparece (incluindo 
espaços e caracteres especiais) e armazene os resultados em um 
dicionário.'''

import os
os.system('cls')

string = input("Digite o texto: ")

alfabeto = { 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}

for conteudo in string.lower():
    if conteudo in alfabeto:
        alfabeto[conteudo] = alfabeto[conteudo] + 1
print(alfabeto)
