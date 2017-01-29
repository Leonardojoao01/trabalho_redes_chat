from tkinter import *
import socket



class Kanvas:
    def __init__(self,root):

        self.fontePadrao = ("Arial", "10")

        self.primeiroContainer = Frame(root)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer["padx"] = 150
        self.primeiroContainer.pack()

        self.segContainer = Frame(root)
        self.segContainer["pady"] = 15
        self.segContainer.pack()

        self.segundoContainer = Frame(root)
        self.segundoContainer["pady"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(root)
        #self.terceiroContainer["pady"] = 23
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(root)
        self.quartoContainer["pady"] = 30
        self.quartoContainer["padx"] = 150
        self.quartoContainer.pack()

        #------------------------------------------------------------------------------------
        self.juju = Label(self.primeiroContainer, text="CHAT - Bem Vindo")
        self.juju["font"] = self.fontePadrao
        self.juju.pack()


        #----------------
        self.ipLabel = Label(self.segContainer, text="IP: ")
        self.ipLabel.pack(padx=0, side=LEFT)

        self.ip = Label(self.segContainer, text="")
        self.ip.pack(padx=0, side=LEFT)

        self.host_label = Label(self.segContainer, text="Host: ")
        self.host_label.pack(padx=0, side=LEFT)

        self.host = Label(self.segContainer, text="")
        self.host.pack(padx=0, side=LEFT)

        dados1, dados2 = self.get_ip()

        self.set_text(dados1, self.ip, dados2, self.host)
        #----------------

        self.conversaLabel = Label(self.segundoContainer, text="Conversa", font=self.fontePadrao, width=90)
        self.conversaLabel.pack(padx=30, side=LEFT)

        self.loginLabel = Label(self.segundoContainer, text="Pessoas Logadas", font=self.fontePadrao, width=50)
        self.loginLabel.pack(padx=30, side=LEFT)




        self.conversa = Label(self.terceiroContainer, text="", bg="grey", width=90, height=20)
        self.conversa.pack(padx=10, side=LEFT)

        self.login = Label(self.terceiroContainer, text="", bg="white", width=30, height=20)
        self.login.pack(padx=50, side=LEFT)




        self.nome = Entry(self.quartoContainer)
        self.nome["width"] = 100
        #self.nome["height"] = 20
        #self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
        # self.conv = Entry(self.quartoContainer, width=100, height=5)
        # self.conv.pack(padx=0, side=LEFT)

        # self.set_text("akjsdklajksd", self.juca)

        #----------------------------------------------------
        self.enviar = Button(self.quartoContainer)
        self.enviar["text"] = "Autenticar"
        self.enviar["font"] = ("Calibri", "8")
        self.enviar["width"] = 12
        self.enviar["command"] = self.set_text2
        self.enviar.pack()

        #self.set_text("juca", self.conversa)

    def set_text2(self):
        #print("Entrou", self.nome.get())
        #juca = self.nome.get()
        #print(juca)
        #self.conversa["text"] = str(self.nome.get())

        usuario = self.nome.get()

        if usuario == "us":
            self.conversa["text"] = "Autenticado"
        else:
            self.conversa["text"] = "Erro na autenticação"


    def set_text(self, master=None, lab=None, master2=None, lab2=None):

        lab['text'] = master

        if master2 != None:
            lab2['text'] = master2

    def get_ip(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))

        HOST = s.getsockname()[0]     # Endereco IP do Servidor
        PORT = "5000"            # Porta que o Servidor esta

        return HOST, PORT




instancia=Tk()
Kanvas(instancia)
instancia.mainloop()
