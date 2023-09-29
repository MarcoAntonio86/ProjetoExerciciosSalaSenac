import random
import os
os.system('cls')

def numero_aleatorio():
    return random.randint(1, 10)

numero = numero_aleatorio()

tentativas = 0

for tentativas in range(3):
  valor = int(input('Tentativa {}: Informe um número de 1 a 10: '.format(tentativas + 1)))

if valor == numero:
    print('Acertou')
    print(f' O numero sorteado foi: {numero}')
    
else:
    if tentativas < 2:
           print('Errou')
           print(f' O numero sorteado foi: {numero}')
    else:
           print('Errou')
           print(f' O numero sorteado foi: {numero}')
   





