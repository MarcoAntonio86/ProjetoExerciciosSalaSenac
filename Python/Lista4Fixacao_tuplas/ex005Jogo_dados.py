import random

dado = (1, 2, 3, 4, 5, 6)

jogada1 = random.choice(dado)

print(f'A jogada 1 deu {jogada1}')

jogada2 = random.choice(dado)

print(f'A jogada 1 deu {jogada2}')

if jogada2 >= jogada1:
     print('You are win')

else:
     print(f'you are losing')



