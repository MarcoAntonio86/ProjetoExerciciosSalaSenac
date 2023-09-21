def verficar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    

valor = float(input('Informe um valor: '))
resultado = verficar_par(valor)
print(f'O resultado é {resultado} ')