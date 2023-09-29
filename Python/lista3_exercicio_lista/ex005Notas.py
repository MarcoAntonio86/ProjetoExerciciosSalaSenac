lista_notas = []
nota = 0
soma_da_lista = 0
soma = 0
divisor_media = 0

while nota != -1:
    nota = int(input('Informe uma nota: '))
    if nota != -1:
      lista_notas.append(nota)

print(f'As notas são: {lista_notas}')


for soma in lista_notas:
    soma_da_lista += soma
    divisor_media += 1


media = soma_da_lista / divisor_media

tupla_lista_numeros = (lista_notas) 

tupla_soma_da_lista = (soma_da_lista)

tupla_divisor_media = (divisor_media)

tupla_media = (media)


print(f'A soma das notas será de {soma_da_lista}')
print(f'A media das notas será de {media}')

if media >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')

print('Fim do sistema')




