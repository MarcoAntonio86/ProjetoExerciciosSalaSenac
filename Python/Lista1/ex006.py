menu = ('--------Programa de calculo ------------ \n'
        '# Informe dois número que queira fazer a operação matemática \n'
        '# Em caso de soma use + \n'
        '# Em caso de subtracao use - \n'
        '# Em caso de multiplicacao use * \n'
        '# Em caso de divisao use / \n')
print(menu)

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))
resultado = 0
sinal = input('Informe o sinal desejado para a operação: ')

if sinal == '+':
    resultado = n1 + n2
elif sinal == '-':
    resultado = n1 - n2
elif sinal == '*':
    resultado = n1 * n2
elif sinal == '/':
    resultado = n1 / n2

print('O resultado da operação é: {:.2f}'.format(resultado))

if resultado % 2 == 0:
    print('O resultado é par')
else:
    print('O resultado é impar')

if resultado.is_integer():
    print('O resultado é um número inteiro')
else:
    print('O resultado é um número decimal')