salBrut = float(input('Informe o salario bruto: R$ '))
IR = salBrut * 11 / 100
INSS =  salBrut * 8 /100
contSindic = salBrut * 5 / 100
salLiqu = salBrut - IR - INSS - contSindic

print('O valor do IR a pagar será de R$ {:.2f} \n O INSS a recolher será de R$ {:.2f} \n A contribuição social será de R$ {:.2f} \n Sua remuneração liquida será de R$ {:.2f}' .format(IR, INSS, contSindic, salLiqu))
