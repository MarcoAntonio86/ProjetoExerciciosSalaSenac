from tkinter import *


def calcular_tabuada():
    num = int(numero_entry.get())
    resultado = ''
    for c in range(11):
        resultado += f'{num} x {c} = {num * c}\n'
    resultado_label.config(text=resultado)


janela = Tk()
janela.title('Tabuada de um Número')
janela.geometry('400x300')


texto_numero = Label(janela, text='Informe um número:')
texto_numero.pack(padx=10, pady=10)

numero_entry = Entry(janela)
numero_entry.pack(padx=10, pady=10)

botao_calcular = Button(janela, text='Calcular Tabuada', command=calcular_tabuada)
botao_calcular.pack(padx=10, pady=10)

resultado_label = Label(janela, text='')
resultado_label.pack(padx=10, pady=10)


janela.mainloop()
