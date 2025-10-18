import tkinter as tk
from tkinter import ttk, messagebox, filedialog

banco = tk.Tk()
banco.title("banco")
banco.geometry("363x663")
banco.config(bg="#0761B0")

def Pix():
    pix = tk.Toplevel(banco)
    pix.title("pix")
    pix.geometry("363x663")
    pix.mainloop()

def Pagar():
    pagar = tk.Toplevel(banco)
    pagar.title("pagar")
    pagar.geometry("363x663")
    pagar.mainloop()

def Recargadecelular():
    Recargadecelular = tk.Toplevel(banco)
    Recargadecelular.title("Recarga de celular")
    Recargadecelular.geometry("363x663")
    Recargadecelular.mainloop()

def Transferir():
    transferir = tk.Toplevel(banco)
    transferir.title("Tranferir")
    transferir.geometry("363x663")
    transferir.mainloop()

texto = tk.Label(banco, text="Bem vindo ao Pybank!", bg="#0761B0", font="Arial")
texto.pack(pady=20)
pix = tk.Button(banco, text="Pix", command=Pix)
pix.place(x=30, y=78)
pagar = tk.Button(banco, text="Pagar", command=Pagar)
pagar.place(x=100, y=78)
recargadecelular = tk.Button(banco, text="Recarga de celular", command=Recargadecelular)
recargadecelular.place(x=170, y=78)
transferir = tk.Button(banco, text="Transferir", command=Transferir)
transferir.place(x=290, y=78)
sair = tk.Button(banco, text="Sair", command=banco.destroy, bg="red")
sair.place(x=175, y= 120)
banco.mainloop()