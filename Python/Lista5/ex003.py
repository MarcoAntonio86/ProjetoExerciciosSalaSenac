def separador_vogal_consoante(palavra):
    vogal = 0
    consoante = 0
    for letra in palavra:
        if letra in "aeiou":
            vogal += 1
        else:
            consoante += 1
    return vogal, consoante


palavra = input('Informe uma palavra: ')
vogal, consoante = separador_vogal_consoante(palavra)
print(f'A palavra tem {vogal} vogais e {consoante} consoantes.')