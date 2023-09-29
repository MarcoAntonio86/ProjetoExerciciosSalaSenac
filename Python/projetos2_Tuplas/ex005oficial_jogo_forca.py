import random


acertos = 0

palavras = ('marco', 'antonio', 'braga', 'lima')

jogador = input('Informe o seu nome: ')

print(f'Boa sorte {jogador}, vai precisar  !')

palavra_sorteada = random.choice(palavras)

chute = ''

limite = 10


while limite > 0 and acertos != len(palavra_sorteada): # pode se usar no lugar no diferente (!=) o sinal de menor
    chute = input('Informe a letra: ')
    if chute in palavra_sorteada:
        print('Você acertou !')

        acertos += palavra_sorteada.count(chute)  # Incrementa o número de acertos corretamente
    else:
        print('Você errou !')
    

   
    print(f'Número de acertos: {acertos}')

    limite -= 1


print(f'Fim do jogo !')

    


