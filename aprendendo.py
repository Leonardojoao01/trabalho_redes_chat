from tkinter import *

class Kanvas:
    def __init__(self,root):

        # self.canvas1 = Canvas(raiz, width=200, height=200, cursor='X_cursor', bd=5, bg='dodgerblue')
        # self.canvas1.pack(side=LEFT)
        #
        # self.canvas2 = Canvas(raiz, width=200, height=200, cursor='dot', bd=5, bg='purple')
        # self.canvas2.pack(side=LEFT)
        # #self.canvas2["text"] = "Autenticado"
        self.fontePadrao = ("Arial", "10")


        self.primeiroContainer = Frame(root)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer["padx"] = 150
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(root)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(root)
        self.terceiroContainer["pady"] = 30
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(root)
        self.quartoContainer["pady"] = 60
        self.quartoContainer.pack()

        #------------------------------------------------------------------------------------
        self.juju = Label(self.primeiroContainer, text="CHAT - Bem Vindo")
        self.juju["font"] = self.fontePadrao
        self.juju.pack()

        self.conversaLabel = Label(self.segundoContainer, text="Conversa", font=self.fontePadrao, width=90)
        self.conversaLabel.pack(padx=10, side=LEFT)

        self.loginLabel = Label(self.segundoContainer, text="Pessoas Logadas", font=self.fontePadrao, width=50)
        self.loginLabel.pack(padx=100, side=LEFT)

        # w = Label(self.terceiroContainer, text="red", bg="red", fg="white")
        # w.pack(pady=10, side=LEFT)
        # w = Label(self.terceiroContainer, text="green", bg="green", fg="black")
        # w.pack(pady=20, side=LEFT)
        # w = Label(self.terceiroContainer, text="blue", bg="blue", fg="white")
        # w.pack(pady=30, side=LEFT)

        self.conversa = Label(self.terceiroContainer, text="", bg="blue", width=90, height=30)
        self.conversa.pack(padx=0, side=LEFT)

        self.login = Label(self.terceiroContainer, text="", bg="red", width=50, height=30)
        self.login.pack(padx=100, side=LEFT)

        # self.teste = Label(self.terceiroContainer, text="lzsdklasjasj")
        # self.teste.pack(padx=10, side=LEFT)
        # self.teste = Label(self.terceiroContainer, text="jucaaaaaaaaa")
        # self.teste.pack(padx=40, side=LEFT)

        # self.juca = Label(self.quartoContainer, text="", bg="blue", fg="white", width=150)
        # self.juca.pack(side=LEFT)
        #
        # self.set_text("akjsdklajksd", self.juca)

    def set_text(self, master=None, lab=None):

        lab['text'] = master

instancia=Tk()
Kanvas(instancia)
instancia.mainloop()
