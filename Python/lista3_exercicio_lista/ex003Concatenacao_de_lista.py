lista1 = []
lista2 = []

while len(lista1) < 10 and len(lista2) < 10:
    numero1 = int(input('Informe um numero da lista 1: '))
    numero2 = int(input('Informe um numero da lista 2: '))
    lista1.append(numero1)
    lista2.append(numero2)
print(f'Os numeros da lista1 são: {lista1}')
print(f'Os numeros da lista2 são: {lista2}')
print(f'Os numeros da lista1 e da lista2 são: {lista1 + lista2}')