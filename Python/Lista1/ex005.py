arquivo = float(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade de download em Mbps: '))
tamanho_bits =  arquivo*8
tempo = tamanho_bits/velocidade
minutos = tempo/60

print('O tempo de download foi de {:.4f} minutos'.format(minutos))
