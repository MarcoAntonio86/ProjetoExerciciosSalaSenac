lista_numeros = []
soma_da_lista = 0
soma = 0
divisor_media = 0

while True:
   numero = int(input('Informe um numero: '))
   lista_numeros.append(numero)
   pergunte = input('Deseja continuar? [S/N] ').strip().upper()
   if pergunte == 'N':
       break
   
print(f'Os números da lista são:  {lista_numeros}')

for soma in lista_numeros:
    soma_da_lista += soma
    divisor_media += 1


media = soma_da_lista / divisor_media

tupla_lista_numeros = (lista_numeros) 

tupla_soma_da_lista = (soma_da_lista)

tupla_divisor_media = (divisor_media)

tupla_media = (media)

print(f'A tupla da lista notas do  aluno será de {tupla_lista_numeros}')

print(f'A tupla soma notas do aluno será de {tupla_soma_da_lista}')

print(f'A tupla do divisor da media será de {tupla_divisor_media}')

print(f'A tupla média será de {tupla_media}')


