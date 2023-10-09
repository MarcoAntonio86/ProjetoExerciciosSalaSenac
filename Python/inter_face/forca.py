from tkinter import *
import random

# Função para verificar o chute do jogador
def verificar_chute():
    global acertos, limite
    chute = chute_entry.get()
    chute_entry.delete(0, END)

    if chute in palavra_sorteada:
        acertos += palavra_sorteada.count(chute)
    else:
        resultado_label.config(text='Você errou!')

    resultado_label.config(text=f'Número de acertos: {acertos}')
    limite -= 1

    if acertos == len(palavra_sorteada):
        resultado_label.config(text='Você venceu o jogo! Parabéns!')
        chute_entry.config(state='disabled')
        botao_verificar.config(state='disabled')
    elif limite == 0:
        resultado_label.config(text=f'Você perdeu! A palavra era "{palavra_sorteada}".')
        chute_entry.config(state='disabled')
        botao_verificar.config(state='disabled')

# Configuração inicial
acertos = 0
palavras = ['marco', 'antonio', 'braga', 'lima']



# Criação da janela
janela = Tk()
janela.title('Jogo de Adivinhação de Palavras')
janela.geometry('400x300')

# Elementos da interface gráfica
texto_orientacao = Label(janela, text=f'Bem-vindo(a)! Tente adivinhar a palavra:')
texto_orientacao.pack(padx=10, pady=10)

chute_entry = Entry(janela)
chute_entry.pack(padx=10, pady=10)

botao_verificar = Button(janela, text='Verificar', command=verificar_chute)
botao_verificar.pack(padx=10, pady=10)

resultado_label = Label(janela, text='')
resultado_label.pack(padx=10, pady=10)

# Variáveis do jogo
palavra_sorteada = random.choice(palavras)
limite = 10

# Inicializa a janela principal
janela.mainloop()
