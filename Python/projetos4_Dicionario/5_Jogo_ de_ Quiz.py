'''Crie um jogo de quiz com várias perguntas e opções de resposta. Use um dicionário 
para armazenar as perguntas, opções de resposta e a resposta correta. O programa 
deve permitir que os jogadores escolham uma pergunta, forneçam uma resposta e 
mostrar se a resposta está correta ou não.'''

import os
os.system('cls')

escolha = {}
c = 0
def pergunta_1():
    pergunta = input('Qual é a capital do Brasil? ').strip().upper()
    if pergunta == 'BRASÍLIA':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_2():
    pergunta = input('Qual é o nome do presidente do Brasil? ').strip().upper()
    if pergunta == 'LULA':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_3():
    pergunta = input('Qual é a capital do estado do Pará? ').strip().upper()
    if pergunta == 'BELEM':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_4():
    pergunta = input('Qual é o nome do governador do estado do Pará? ').strip().upper()
    if pergunta == 'HELDER BARBALHO':  
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_5():
    pergunta = input('Qual é o nome da linguagem que estamos aprendendo? ').strip().upper()
    if pergunta == 'PYTHON':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_6():
    pergunta = input('Qual é o nome da proxima linguagem que vamos aprender? ').strip().upper()
    if pergunta == 'JAVA':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_7():
    pergunta = input('Qual é o nome da linguagem que aprendemos antes da que estamos? ').strip().upper()
    if pergunta == 'JAVASCRIPT':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_8():
    pergunta = input('Qual é a melhor para mobile? ').strip().upper()
    if pergunta == 'JAVA':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_9():
    pergunta = input('Qual é a melhor para web? ').strip().upper()
    if pergunta == 'JAVASCRIPT':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta

def pergunta_10():
    pergunta = input('Qual é a melhor para desktop? ').strip().upper()
    if pergunta == 'PYTHON':
        print('Resposta certa!')
    else:
        print('Resposta errada!')
    return pergunta





while c < 5:
    opcao = input('Escolha perguntas de a a j, lembre-se você só pode escolher até 5 perguntas: ').strip().upper()
    if opcao == 'A':
        escolha['A'] = pergunta_1()
        
    elif opcao == 'B':
        escolha['B'] = pergunta_2()
    
    elif opcao == 'C':
        escolha['C'] = pergunta_3()
        
    elif opcao == 'D':
        escolha['D'] = pergunta_4()
    
    elif opcao == 'E':
        escolha['E'] = pergunta_5()
        
    elif opcao == 'F':
         escolha['F'] = pergunta_6()

    elif opcao == 'G':
        escolha['G'] = pergunta_7()
        
    elif opcao == 'H':
        escolha['H'] = pergunta_8()
    
    elif opcao == 'I':
        escolha['I'] = pergunta_9()
        
    elif opcao == 'J':
        escolha['J'] = pergunta_10()
    
    else:
        print('Opção invalida')
    c += 1

print(escolha)
