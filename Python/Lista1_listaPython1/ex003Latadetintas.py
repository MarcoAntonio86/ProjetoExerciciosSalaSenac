import math
larg = float(input('Infome a largura: '))
alt =  float(input('Informe a altura: '))
area = larg * alt
tinta = area / 3
latas = math.ceil(tinta / 18)
preco = latas * 80





print('A area a ser pintada mede cerca de {:.2f}m2'.format(area))
print('A quantidade de tinta utilizada será de {:.2f} \n A quantidade de latas utilizadas será de {:.2f}  no valor de R$ {:.2f}'.format(tinta, latas , preco))
