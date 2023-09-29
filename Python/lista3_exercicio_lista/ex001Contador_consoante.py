vogal = 0
consoante = 0
palavra = []

while len(palavra) < 10:
    letra = input('Informe uma letra: ')
    palavra.append(letra)

print(f'A plavra é {palavra}')

for string in palavra:
    if string in "aeiou":
        vogal += 1
        
    else:
        consoante += 1

print(f'A palavra tem {vogal} vogais e {consoante} consoantes.')