import tkinter as tk

class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tela inicial")
        self.config(bg="#0761B0")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.telas = {}

        for T in (paginalogin, paginaprincipal):
            nome_tela = T.__name__
            frame = T(parent=container, controller=self)
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("paginalogin")
    
    def mostrar_tela(self, nome_tela):
        tela = self.telas[nome_tela]
        tela.tkraise()

class paginalogin(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Usuário:").pack(pady=5)
        self.entry_usuario = tk.Entry(self)
        self.entry_usuario.pack()

        tk.Label(self, text="Senha:").pack(pady=5)
        self.entry_senha = tk.Entry(self, show="*")
        self.entry_senha.pack()

        self.lbl_msg = tk.Label(self, text="", fg="red")
        self.lbl_msg.pack()

        tk.Button(self, text="Login", command=self.verificar_login).pack(pady=10)

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if usuario == "carol" and senha == "12345":
            self.controller.mostrar_tela("paginaprincipal")
        else:
            self.lbl_msg.config(text="Usuário ou senha inválidos!")

class paginaprincipal(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller


if __name__ == "__main__":
    app = Aplicativo()
    app.mainloop()


#exportação de imagens
