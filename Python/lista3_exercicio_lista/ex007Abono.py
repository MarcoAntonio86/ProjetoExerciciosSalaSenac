salarios = []
salario = 0
abonos = []
salarios_minimos = 0

while salario != -1:
    salario = float(input('Informe o salario bruto: R$ '))
    if salario != -1:
        salarios.append(salario)

print(f'A lista de salarios será de {salarios}')

for salario in salarios:
    if salario >= 1000:
        abono = salario * 20/100
    else:
        abono = 100
        salarios_minimos += 1
    abonos.append(abono)

total_gasto_abonos = sum(abonos)
num_colaboradores = len(salarios)
maior_abono = max(abonos)

for salario, abono in zip(salarios, abonos):
    print(f'Salário: R$ {salario:.2f} - Abono: R$ {abono:.2f}')

print(f'Foram processados {num_colaboradores} colaboradores')
print(f'Total gasto com abonos: R$ {total_gasto_abonos:.2f}')
print(f'Valor mínimo pago a {salarios_minimos} colaboradores')
print(f'Maior valor de abono pago: R$ {maior_abono:.2f}')