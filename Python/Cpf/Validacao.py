# primeiro calculo multiplicar os primeiros numeros (9 numeros) de 10 ate 2, soma divide por 11 para dar resto % e faz 11 - resto
# segundo é quase iqual ao primeiro vou multiplicar os primeiros numeros de 11 ate 2 (o dois sera para o digito discoberto acima), soma divide por 11 para dar resto % e faz 11 - resto
# se o codigo acima o valor for maior que 9 converte a zero

cpf = []
numero = 0

def valida_cpf(cpf):
    while len(cpf) < 11:
        numero = int(input('Informe um numero: '))
        cpf.append(numero)
        print(cpf)
        

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
    num10 = num10 * 2
    
    soma = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    resto = soma % 11
    digito = 11 - resto
    
    if digito < 2 or digito > 9:
        digito = 0

    num11 = digito


def validacao(cpf):
    if num10 == cpf[9] and num11 == cpf[10]:
        print('Cpf valido')
    else:
        print('Cpf invalido')
   


    
valida_cpf(cpf)
print(cpf[0])
algoritimo1(cpf)





