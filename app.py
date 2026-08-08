import tkinter as tk
from tkinter import messagebox


def hello_mundo():
    messagebox.showinfo("Mensagem", "Hello, mundo!")


janela = tk.Tk()
janela.title("Meu primeiro programa")
janela.geometry("400x200")

botao = tk.Button(
    janela,
    text="Clique aqui",
    command=hello_mundo
)

botao.pack(pady=70)

janela.mainloop()