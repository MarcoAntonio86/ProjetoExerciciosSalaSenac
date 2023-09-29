def verificar_par(numero):
    return numero % 2 == 0

valores = []
quantidade_valores = int(input('Informe a quantidade de valores: '))

for i in range(quantidade_valores):
    valor = float(input(f'Informe o valor {i+1}: '))
    valores.append(valor)

resultados = [verificar_par(valor) for valor in valores]

for i, resultado in enumerate(resultados):
    print(f'O resultado para o valor {valores[i]} é {resultado}')