v1 = 0
v2 = 0
v3 = 0
v4 = 0

while True:
  print('1- josé \n 2- fulano \n 3- nulo \n 4- branco')
  voto = input('Informe seu voto: ')
  if voto == '1':
    v1 += 1
  elif voto == '2':
    v2 += 1
  elif voto == '3':
    v3 += 1
  elif voto == '4':
    v4 += 1
  else:
    break

print (f'Votos para jose: {v1} \n Votos para fulano: {v2} \n Votos para nulo: {v3} \n Votos para branco: {v4}')

porc1 = (v1 / (v1 + v2 + v3 + v4)) * 100
porc2 = (v2 / (v1 + v2 + v3 + v4)) * 100
porc3 = (v3 / (v1 + v2 + v3 + v4)) * 100
porc4 = (v4 / (v1 + v2 + v3 + v4)) * 100

print (f'Porcentagem de votos de jose: {porc1:.2f} \n Porcentagem de votos de fulano: {porc2:.2f} \n Porcentagem de votos de nulo: {porc3:.2f} \n Porcentagem de votos de branco: {porc4:.2f}')