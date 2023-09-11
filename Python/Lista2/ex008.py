
entrada = int(input('Informe o ano de entrada: '))
atual = int(input('Informe o ano atual: '))
salario = float(input('Informe o salario mensal: '))
porc = float(input('Informe a primeria porcentagem de reajuste: '))
tempo_empresa = atual - entrada
aum = salario * porc / 100
bruto = salario + aum
print(f'O tempo de empresa é de {tempo_empresa} anos')

print(bruto)

for c in range (tempo_empresa ):
   porc = porc * 2
   bruto = bruto + aum
   
print(porc)    

print('O salario final é de R$ {:.2f}'.format(bruto))


