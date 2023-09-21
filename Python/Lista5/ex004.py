
lista = []

def encontrar_menor_elemento(lista):
    menor = lista[0]
    for elemento in lista:
        if elemento < menor:
            menor = elemento
    return menor


while True:
    numero = int(input('Informe um numero: '))
    lista.append(numero)
    pergunte = input('Deseja continuar? [S/N] ').strip().upper()
    if pergunte == 'N':
        break

print(f'Os numeros da lista são: {lista}')
print(f'O menor elemento da lista é {encontrar_menor_elemento(lista)}')

