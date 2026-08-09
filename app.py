import tkinter as tk

def abrir_modal(titulo, texto, pos_x, pos_y):
    modal = tk.Toplevel(janela)
    modal.title(titulo)
    modal.geometry(f"260x120+{pos_x}+{pos_y}")
    modal.transient(janela)
    modal.resizable(False, False)

    tk.Label(
        modal,
        text=texto,
        wraplength=220,
        justify="center",
        padx=20,
        pady=20
    ).pack()

    tk.Button(modal, text="Fechar", command=modal.destroy).pack(pady=(0, 10))

def hello_mundo():
    abrir_modal("Mensagem", "Hello, mundo!", 50, 50)

def funtion2():
    abrir_modal("Mensagem", "Segunda função acionada!!!!", 300, 150)

janela = tk.Tk()
janela.title("Meu primeiro programa")
janela.geometry("400x200")

botao = tk.Button(janela, text="Clique aqui", command=hello_mundo)
botao2 = tk.Button(janela, text="Clique aqui", command=funtion2)

botao.pack(pady=70)
botao2.pack(pady=10)

janela.mainloop()