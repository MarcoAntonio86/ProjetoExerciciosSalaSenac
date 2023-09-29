import statistics

lista_numeros = []

quantidade_itens_lista = int(input('Informe a quantidade de itens da lista: '))

for i in range(quantidade_itens_lista):
    numero = int(input('Informe um numero: '))
    lista_numeros.append(numero)

print(f'A lista de números é {lista_numeros}')

print('A media é {}'.format(statistics.mean(lista_numeros)))


    


