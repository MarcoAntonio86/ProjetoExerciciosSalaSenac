

import os
os.system('cls')


cpf = []
numero = 0
list_cpf = []

def valida_cpf(cpf):
    while len(cpf) < 11:
        numero = input('Informe um número: ')
        
        
        if numero.isdigit():
            numero = int(numero)
            cpf.append(numero)
            print(cpf)
        else:
            print('Valor inválido. Por favor, informe um número inteiro.')
        
def algoritimo1(cpf):
    num1 = cpf[0] * 10
    num2 = cpf[1] * 9
    num3 = cpf[2] * 8   
    num4 = cpf[3] * 7
    num5 = cpf[4] * 6
    num6 = cpf[5] * 5
    num7 = cpf[6] * 4
    num8 = cpf[7] * 3
    num9 = cpf[8] * 2
    
    soma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9
    resto = soma % 11
    digito = 11 - resto
    
    if digito < 2 or digito > 9:
        digito = 0

    num10 = digito

    return num10

def algoritimo2(cpf):
    num1 = cpf[0] * 11
    num2 = cpf[1] * 10
    num3 = cpf[2] * 9
    num4 = cpf[3] * 8
    num5 = cpf[4] * 7
    num6 = cpf[5] * 6
    num7 = cpf[6] * 5
    num8 = cpf[7] * 4
    num9 = cpf[8] * 3
    num10 = algoritimo1(cpf) * 2
    
    soma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    resto = soma % 11
    digito = 11 - resto
    
    if digito < 2 or digito > 9:
        digito = 0

    num11 = digito

    return num11


def validacao(cpf):
    num10 = algoritimo1(cpf)
    num11 = algoritimo2(cpf)

    if num10 == cpf[9] and num11 == cpf[10]:
        return True
    else:
        return False


list_cpf = []  

while True:
    cpf = []  
    valida_cpf(cpf)
    if validacao(cpf):
        list_cpf.append(cpf)  
        print('Cpf válido')
    else:
        print('Cpf inválido')
    pergunta = input('Deseja continuar? S/N: ') .strip().upper()
    if pergunta == 'N':
        break

print(list_cpf)




    