ws = []
unix = []
linux = []
netware = []
marcOs = []
outros = []

soma = 0
cws = 0
cunix = 0
clinux = 0
cnetware = 0
cmarcOs = 0
coutros = 0

print('------MENU------- \n'
      'vote 1 para windows \n'
      'vote 2 para unix \n'
      'vote 3 para linux \n'
      'vote 4 para netware \n'
      'vote 5 para marcOS \n'
      'vote 6 para outros \n'
      'vote 0 para sair')

while True:
    votos = int(input('Informe o numero de votos: '))
    if votos == 1:
        ws.append(votos)
        cws += 1
    elif votos == 2:
        unix.append(votos)
        cunix += 1
    elif votos == 3:
        linux.append(votos)
        clinux += 1
    elif votos == 4:
        netware.append(votos)
        cnetware += 1
    elif votos == 5:
        marcOs.append(votos)
        cmarcOs += 1
    elif votos == 6:
        outros.append(votos)    
        coutros += 1
    elif votos == 0:
        break
    else:
        print('Opção inválida. Digite o número correspondente à opção desejada.')

print(f'Windows: {ws}')
print(f'Unix: {unix}')
print(f'Linux: {linux}')
print(f'Netware: {netware}')
print(f'MarcOS: {marcOs}')
print(f'Outros: {outros}')

soma = cws + cunix + clinux + cnetware + cmarcOs + coutros

print(f'Total de votos: {soma}')

porcent_ws = (cws / soma) * 100
porcent_unix = (cunix / soma) * 100
porcent_linux = (clinux / soma) * 100
porcent_netware = (cnetware / soma) * 100
porcent_marcOs = (cmarcOs / soma) * 100
porcent_outros = (coutros / soma) * 100

print(f'Porcentagem de Windows: {porcent_ws :.2f}')
print(f'Porcentagem de Unix: {porcent_unix:.2f}')
print(f'Porcentagem de Linux: {porcent_linux :.2f}')
print(f'Porcentagem de Netware: {porcent_netware :.2f}')
print(f'Porcentagem de MarcOS: {porcent_marcOs :.2f}')
print(f'Porcentagem de Outros: {porcent_outros :.2f}')

