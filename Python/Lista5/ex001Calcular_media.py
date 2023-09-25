def calcular_media(notas):
    return sum(notas) / len(notas)

notas = []
quantidade_notas = int(input('Informe a quantidade de notas: '))

for i in range(quantidade_notas):
    nota = float(input(f'Informe a nota {i+1}: '))
    notas.append(nota)

resultado = calcular_media(notas)
print(f'A média é {resultado}')