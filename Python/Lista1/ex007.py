print (' Responda com S, para sim, ou N, para não.'
       '\n As perguntas estão simbolizadas por P, indo de 1 a 5. \n')

P1 = input("Telefonou para a vítima? ").strip().upper()
P2 = input("Esteve no local do crime? ").strip().upper()
P3 = input("Mora perto da vítima? ").strip().upper()
P4 = input("Devia para a vítima? ").strip().upper()
P5 = input("Já trabalhou com a vítima? ").strip().upper()

Contador_S = 0

if P1 == 'S':
    Contador_S += 1
if P2 == 'S':   
    Contador_S += 1
if P3 == 'S':
    Contador_S += 1
if P4 == 'S':
    Contador_S += 1
if P5 == 'S':
    Contador_S += 1

if Contador_S == 2:
    print('Suspeita')
elif Contador_S in (3, 4):
    print('Cúmplice')
elif Contador_S == 5:
    print('Assassino')
else:
    print('Inocente')



