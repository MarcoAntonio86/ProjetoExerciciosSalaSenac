import math
larg = float(input('Infome a largura: '))
alt =  float(input('Informe a altura: '))
area = larg * alt
tinta = area / 6
latas = math.ceil(tinta / 18)
galoes = math.ceil(tinta / 3.6)
preco = latas * 80
preco2 = galoes * 25
latas_mix = math.ceil((tinta * 1.1) / 18)
galoes_mix = math.ceil(((tinta * 1.1) / 18) / 3.6)
preco_mix = (latas_mix * 80) + (galoes_mix * 25)

print('A area a ser pintada mede cerca de {:.2f}m2'.format(area))
print('A quantidade de tinta utilizada será de {:.2f} \n A quantidade de latas utilizadas será de {:.2f}  no valor de R$ {:.2f}'.format(tinta, latas , preco))
print('A quantidade de galões utilizados será de {:.2f}  no valor de R$ {:.2f}'.format(galoes, preco2))
print(' A mistura das duas modalidade mais um acrecimo de 10% fica em {} latas e {} galões no valor de {}'.format(latas_mix, galoes_mix, preco_mix))