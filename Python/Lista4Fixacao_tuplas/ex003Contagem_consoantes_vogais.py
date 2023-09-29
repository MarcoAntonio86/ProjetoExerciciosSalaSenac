

vogal = 0
consoante = 0
palavra = []


while True:
   letra = input('Informe uma letra: ')
   palavra.append(letra)
   pergunte = input('Deseja continuar? [S/N] ').strip().upper()
   if pergunte == 'N':
       break
   
tupla_palavra = (palavra)
   
print(f'Os números de letras da tupla são:  {tupla_palavra}')

for string in palavra:
    if string in "aeiou":
        vogal += 1
        
    else:
        consoante += 1

    tupla_vogal = (vogal)

    tupla_consoante = (consoante)

print(f'As respectivas tuplas serão {tupla_vogal}, para o toal de vogais e a {tupla_consoante} para o total de consoante.')
        








