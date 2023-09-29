
lista_numero = []

while True:
    numero = int(input('Informe um numero: '))
    lista_numero.append(numero)
    pergunte = input('Deseja continuar? [S/N] ').strip().upper()
    if pergunte == 'N':
        break

print(f'Os números da lista são:  {lista_numero}')
print(f'Os números em ordem decrescente serão:  {sorted(lista_numero, reverse=True)}')
print(f' \n e na ordem crescente serão:  {sorted(lista_numero)}')