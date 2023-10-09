

'''NESSE CÓDIGO, VOCÊ TEM DE AUMENTAR A JANELA PARA VER O RESULTADO'''

from tkinter import *


def soma():
    n1 = float(entry_n1.get())
    n2 = float(entry_n2.get())
    resultado.set(n1 + n2)

def subtracao():
    n1 = float(entry_n1.get())
    n2 = float(entry_n2.get())
    resultado.set(n1 - n2)

def multiplicacao():
    n1 = float(entry_n1.get())
    n2 = float(entry_n2.get())
    resultado.set(n1 * n2)

def divisao():
    n1 = float(entry_n1.get())
    n2 = float(entry_n2.get())
    if n2 == 0:
        resultado.set('Não é possível dividir por zero.')
    else:
        resultado.set(n1 / n2)


janela = Tk()
janela.title('Calculadora')
janela.geometry('400x300')


texto_orientacao = Label(janela, text='Digite os números e escolha a operação:')
texto_orientacao.pack(padx=10, pady=10)

entry_n1 = Entry(janela, width=10)
entry_n1.pack(padx=10, pady=10)

entry_n2 = Entry(janela, width=10)
entry_n2.pack(padx=10, pady=10)

botao_soma = Button(janela, text='+', command=soma)
botao_soma.pack(padx=10, pady=10)

botao_subtracao = Button(janela, text='-', command=subtracao)
botao_subtracao.pack(padx=10, pady=10)

botao_multiplicacao = Button(janela, text='*', command=multiplicacao)
botao_multiplicacao.pack(padx=10, pady=10)

botao_divisao = Button(janela, text='/', command=divisao)
botao_divisao.pack(padx=10, pady=10)

resultado = StringVar()
label_resultado = Label(janela, textvariable=resultado)
label_resultado.pack(padx=10, pady=10)


janela.mainloop()

'''NESSE CÓDIGO, VOCÊ TEM DE AUMENTAR A JANELA PARA VER O RESULTADO'''
