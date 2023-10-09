from tkinter import *

# Função para adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = tarefa_entry.get()
    if tarefa:
        lista.insert(END, tarefa)
        tarefa_entry.delete(0, END)

# Função para remover uma tarefa da lista
def remover_tarefa():
    selected_task = lista.curselection()
    if selected_task:
        index = selected_task[0]
        lista.delete(index)

# Criação da janela
janela = Tk()
janela.title('Lista de Tarefas')
janela.geometry('400x300')

# Elementos da interface gráfica
texto_orientacao = Label(janela, text='Digite a tarefa e clique em Adicionar:')
texto_orientacao.pack(padx=10, pady=10)

tarefa_entry = Entry(janela)
tarefa_entry.pack(padx=10, pady=10)

botao_adicionar = Button(janela, text='Adicionar', command=adicionar_tarefa)
botao_adicionar.pack(padx=10, pady=10)

botao_remover = Button(janela, text='Remover', command=remover_tarefa) # click encima da tarefa, selecione, depois clik em remover
botao_remover.pack(padx=10, pady=10)

lista = Listbox(janela)
lista.pack(padx=10, pady=10)

# Inicializa a janela principal
janela.mainloop()
