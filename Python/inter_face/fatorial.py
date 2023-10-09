from tkinter import *


def calcular_fatorial():
    num = int(numero_entry.get())
    resultado = math.factorial(num)
    resultado_label.config(text=f'O fatorial de {num} é {resultado}')

import math


janela = Tk()
janela.title('Cálculo do Fatorial')
janela.geometry('400x300')


texto_numero = Label(janela, text='Informe um número:')
texto_numero.pack(padx=10, pady=10)

numero_entry = Entry(janela)
numero_entry.pack(padx=10, pady=10)

botao_calcular = Button(janela, text='Calcular Fatorial', command=calcular_fatorial)
botao_calcular.pack(padx=10, pady=10)

resultado_label = Label(janela, text='')
resultado_label.pack(padx=10, pady=10)


janela.mainloop()
