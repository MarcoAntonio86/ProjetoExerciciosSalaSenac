import random

def numero_aleatorio():
    return random.randint(1, 10)

numero = numero_aleatorio()

tentativas = 0

valor = int(input('Informe um numero de 1 a 10: '))




if valor == numero:
    print('Acertou')
    print(numero)
else:
    print('Errou')
    print(numero)
    

