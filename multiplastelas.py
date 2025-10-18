import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema com múltiplas telas")
        self.geometry("400x300")

        # Container para armazenar as telas
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.telas = {}  # dicionário para armazenar as telas

        for T in (LoginPage, PrincipalPage):
            nome_tela = T.__name__
            frame = T(parent=container, controller=self)
            self.telas[nome_tela] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.mostrar_tela("LoginPage")

    def mostrar_tela(self, nome_tela):
        tela = self.telas[nome_tela]
        tela.tkraise()  # traz a tela para frente


class LoginPage(tk.Frame):
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

        if usuario == "admin" and senha == "123":
            self.controller.mostrar_tela("PrincipalPage")
        else:
            self.lbl_msg.config(text="Usuário ou senha inválidos!")


class PrincipalPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Bem-vindo à tela principal!", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Sair", command=lambda: controller.mostrar_tela("LoginPage")).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()


