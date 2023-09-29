ano_entrada = int(input('Informe o ano de entrada: '))
ano_atual = int(input('Informe o ano atual: '))
salario_inicial = float(input('Informe o salário inicial: '))


salario = salario_inicial
porcentagem_aumento = 1.5  

for ano in range(ano_entrada, ano_atual + 1):
    aum = salario * porcentagem_aumento / 100
    salario += aum
    print(f'Ano: {ano}, Salário: R$ {salario:.2f}, Aumento: {aum:.2f}%')
    porcentagem_aumento *= 2  

print(f'O salário final em {ano_atual} é de R$ {salario:.2f}')