i = 1
maior = 0

while i<=5:
    n = int(input('Digite um número: '))

    if n > maior: 
        maior = n
    i += 1

print('O maior número é {}'.format(maior))
