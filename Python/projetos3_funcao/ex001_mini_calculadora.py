
import os
os.system('cls')
def soma(n1, n2):
    return n1 + n2

def subtracao(n1, n2):
    return n1 - n2

def multiplicacao(n1, n2):
    return n1 * n2

def divisao(n1, n2):
    if n2 == 0:
        print('Não é possível dividir por zero.')
        return None
    return n1 / n2

while True:
    n1 = float(input('Informe o primeiro número: '))
    n2 = float(input('Informe o segundo número: '))

    while True:
        sinal = input('Informe o sinal desejado para a operação: ')
        if sinal in ['+', '-', '*', '/']:
            break
        else:
            print('Operação inválida')

    if sinal == '+':
        resultado = soma(n1, n2)
    elif sinal == '-':
        resultado = subtracao(n1, n2)
    elif sinal == '*':
        resultado = multiplicacao(n1, n2)
    elif sinal == '/':
        resultado = divisao(n1, n2)

    if resultado is not None:
        print('O resultado da operação é: {:.2f}'.format(resultado))

    pergunta = input('Deseja continuar? [S/N] ').strip().upper()
    if pergunta == 'N':
        break

print('Fim do programa')
