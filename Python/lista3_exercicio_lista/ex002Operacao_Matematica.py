lista = []
soma = 0
soma_lista = 0


while len(lista) < 5:
    numero = int(input('Informe um numero: '))
    lista.append(numero)
    soma = soma + numero
    soma_lista = soma_lista + soma

print(f'Os numeros da lista são: {lista}')
print(f'A soma da lista é: {soma}')