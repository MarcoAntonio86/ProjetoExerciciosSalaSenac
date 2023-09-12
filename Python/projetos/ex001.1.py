lista_numeros = []
soma_da_lista = 0
#quantidade_itens_lista = 0
soma = 0
divisor_media = 0

while True:
   numero = int(input('Informe um numero: '))
   lista_numeros.append(numero)
   pergunte = input('Deseja continuar? [S/N] ').strip().upper()
   if pergunte == 'N':
       break
   
#print(f'Os números da lista são:  {lista_numeros[0]}')
print(f'Os números da lista são:  {lista_numeros}')

for soma in lista_numeros:
    soma_da_lista += soma
    divisor_media += 1

    

'''for i in lista_numeros:
    soma_da_lista += lista_numeros

print(f'A soma da lista é: {soma_da_lista}')'''

print(f'A soma da lista é: {soma_da_lista}')

print(f'O divisor da media é: {divisor_media}')

media = soma_da_lista / divisor_media

print(f'A media é: {media}')


