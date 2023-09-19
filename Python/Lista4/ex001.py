lista = []
soma_lista = 0
soma = 0
divisor_media = 0

while True:
   numero = int(input('Informe um numero: '))
   lista.append(numero)
   pergunte = input('Deseja continuar? [S/N] ').strip().upper()
   if pergunte == 'N':
       break
   
   print(f'Os numeros da lista são: {lista}')

   for soma in lista:
       soma_lista += soma


tupla_lista = (lista)
tupla_soma_lista = (soma_lista)

print(f'A lista convertida em tupla será de {tupla_lista}')
print(f'E sua soma será de {tupla_soma_lista}')