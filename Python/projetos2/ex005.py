import random

acertos = 0

# Tupla de palavras possíveis
palavras = ('marco', 'antonio', 'braga', 'lima')

jogador = input('Informe o seu nome: ')

print(f'Boa sorte {jogador}, vai precisar!')

# Escolher aleatoriamente uma palavra da tupla
palavra_sorteada = random.choice(palavras)

chute = ''

limite = 10

while limite > 0 and acertos != len(palavra_sorteada):
    chute = input('Informe a letra: ')
    if chute in palavra_sorteada:
        print('Você acertou!')

        # Incrementa o número de acertos corretamente
        acertos += palavra_sorteada.count(chute)
    else:
        print('Você errou!')

    print(f'Número de acertos: {acertos}')

    limite -= 1

print(f'Fim do jogo!')
