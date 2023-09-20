lista1 = []
lista2 = []
lista3 = []

while len(lista1) < 10 and len(lista2) < 10 and len(lista3) < 10:
    numero1 = int(input('Informe um numero da lista 1: '))
    numero2 = int(input('Informe um numero da lista 2: '))
    numero3 = int(input('Informe um numero da lista 3: '))
    lista1.append(numero1)
    lista2.append(numero2)
    lista3.append(numero3)
print(f'Os numeros da lista1 são: {lista1}')
print(f'Os numeros da lista2 são: {lista2}')
print(f'Os numeros da lista3 são: {lista3}')
print(f'Os numeros da lista1 e da lista2 são: {lista1 + lista2 + lista3}')