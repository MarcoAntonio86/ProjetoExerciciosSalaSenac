populacao1 = float(input('Informe a primeira populacao: '))
populacao2 = float(input('Informe a segunda populacao: '))
anos = 0

while populacao1 < populacao2:
    populacao1 = populacao1 + (populacao1 * 0.03)
    populacao2 = populacao2 + (populacao2 * 0.015)
    anos += 1

print(f'A diferença de população é de {anos} anos')
