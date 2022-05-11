import tkinter.messagebox
from tkinter import *
import pyperclip
import random


def gerar_senha():
    senha = ''
    caracteres = 'ABCDEF0123456789'
    try:
        largura_senha = int(opcao_menu.get())
    except ValueError:
        return ''
    for x in range(largura_senha):
        senha += random.choice(caracteres)
        texto_senha.delete(0, END)
        texto_senha.insert(0, f'{senha}')
        pyperclip.copy(senha)
    tkinter.messagebox.showinfo(title=None, message='Senha copiada')


lista_menu = [8, 16, 32, 64, 128]

janela = Tk()
janela.geometry('400x200')

janela.title('PyHex - Gerador de senhas')

opcao_menu = StringVar(janela)
opcao_menu.set('Largura')

menu = OptionMenu(janela, opcao_menu, *lista_menu)
menu.place(width=10, height=5, x=2, y=2)
menu.pack()

botao = Button(janela, text='Gerar Senha', command=gerar_senha)
botao.place(width=80, height=20, x=160, y=50)

texto_senha = Entry(janela, fg='red')
texto_senha.place(width=300, height=20, x=50, y=90)

janela.configure(background='#85929e')
janela.resizable(False, False)
janela.mainloop()
