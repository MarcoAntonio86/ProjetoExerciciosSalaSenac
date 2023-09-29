def separar_vogal_consoante(palavra):
    vogal = 0
    consoante = 0
    for letra in palavra:
        if letra in "aeiou":
            vogal += 1
        else:
            consoante += 1
    return vogal, consoante

palavras = []
quantidade_palavras = int(input('Informe a quantidade de palavras: '))

for i in range(quantidade_palavras):
    palavra = input(f'Informe a palavra {i+1}: ')
    palavras.append(palavra)

for palavra in palavras:
    vogal, consoante = separar_vogal_consoante(palavra)
    print(f'A palavra "{palavra}" tem {vogal} vogais e {consoante} consoantes.')