quant = int(input('Informe a quantidade de temperaturas desejadas: '))
temp = float(input('Informe a temperatura: '))

maior = temp
menor = temp
media = temp

for i in range(quant - 1): # quant - 1 é pelo fato de contar de 0 ao número digitado, ex.: 5, logo tem de colocar -1 para contar de 0 a 4 e dar 5
   temp = float(input('Informe a temperatura: '))
   if temp < menor:
      menor = temp
   if temp > maior:
      maior = temp

   media += temp


media = media / (quant)

print(f'A temperatura mais baixa foi {menor:.2f} e a mais alta foi {maior:.2f}')
print(f'A media das temperaturas foi de {media:.2f}')
    
