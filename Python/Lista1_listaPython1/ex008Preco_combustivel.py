tipo = input('Informe o tipo de combustivel, (A) álcool ou (G) gasolina: ').strip().upper()
litros = float(input('Informe a quantidade de litros: '))
vlrA = 1.90
vlrG = 2.50
descA1 = 1.90 * 3 / 100
descA2 = 1.90 * 5 / 100
descG1 = 2.50 * 4 / 100
descG2 = 2.50 * 6 / 100
resultado = 0



if tipo == 'A' and litros <=20:
    resultado = litros * (vlrA - descA1)
elif tipo == 'A' and litros > 20:
    resultado = litros * (vlrA - descA2)
elif tipo == 'G' and litros <= 20:
    resultado = litros * (vlrG - descG1)
elif tipo == 'G' and litros > 20:
    resultado = litros * (vlrG - descG2)

print ('O valor a ser pago é de R$ {:.2f}'.format(resultado))
