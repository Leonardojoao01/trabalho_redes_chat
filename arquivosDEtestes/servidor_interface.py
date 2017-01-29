from tkinter import *
from threading import Thread
import socket

from servidor import *



class servidor_interface(Thread):
    subject_list = []
    def __init__(self,root, obj):

        #-----São as frames(áreas), utilizadas para salvar conteúdo dentro delas-----
        #subject_list = []
        Thread.__init__(self)

        object_servidor = servidor()
        object_servidor.start()

        self.fontePadrao = ("Arial", "15")

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
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(root)
        self.quartoContainer["pady"] = 30
        self.quartoContainer["padx"] = 150
        self.quartoContainer.pack()

        #-----------------------------------------------------------------------

        #-----------------------------------------------------------------------
        self.title_label = Label(self.primeiroContainer, text="CHAT - Servidor")
        self.title_label["font"] = self.fontePadrao
        self.title_label.pack()


        #-------Mostra o ip do Servidor, onde os clientes devem conectar--------
        #-----------------------------------------------------------------------
        self.host_label = Label(self.segContainer, text="IP: ")
        self.host_label.pack(padx=0, side=LEFT)

        self.host = Label(self.segContainer, text="")
        self.host.pack(padx=0, side=LEFT)

        self.port_label = Label(self.segContainer, text="Host: ")
        self.port_label.pack(padx=0, side=LEFT)

        self.port = Label(self.segContainer, text="")
        self.port.pack(padx=0, side=LEFT)

        #-----------Nesse ponto pega o ip e salva/mostra na tela----------------

        inf_host, inf_port = self.get_ip()         # Pega o IP e HOST da máquina

        self.set_text(inf_host, self.host, inf_port, self.port)
        #-----------------------------------------------------------------------
        #-----------------------------------------------------------------------

        #----------Campo onde mostra as conversas e pessoas logadas-------------
        self.subject_label = Label(self.segundoContainer, text="Conversa", width=90)
        self.subject_label.pack(padx=0, side=LEFT)

        self.users_label = Label(self.segundoContainer, text="Pessoas Logadas", width=50)
        self.users_label.pack(padx=0, side=LEFT)


        self.subject = Label(self.terceiroContainer, text="", bg="grey", width=90, height=20)
        self.subject.pack(padx=10, side=LEFT)

        self.users = Label(self.terceiroContainer, text="", bg="white", width=30, height=20)
        self.users.pack(padx=50, side=LEFT)

        #-----------------------------------------------------------------------

        self.nome = Entry(self.quartoContainer)
        self.nome["width"] = 100
        self.nome.pack(side=LEFT)

        #----------------------------------------------------
        self.enviar = Button(self.quartoContainer)
        self.enviar["text"] = "Enviar"
        self.enviar["font"] = ("Calibri", "8")
        self.enviar["width"] = 12
        self.enviar["command"] = self.set_subject
        self.enviar.pack()

        #root.mainloop()

        #self.set_text("juca", self.conversa)

    def set_subject(self):

        subject_all = ""

        subject_field = self.nome.get()

        self.subject_list.append(subject_field+"\n")

        for subject_unique in self.subject_list:
             subject_all = subject_all + subject_unique #+ "\n"

        self.subject['text'] = subject_all


    def set_text(self, master=None, lab=None, master2=None, lab2=None):

        lab['text'] = master

        if master2 != None:
            lab2['text'] = master2


    #----------------Conecta no google para descobrir o ip local----------------
    #--------------------------------------------Pode ser qq endereço externo---
    def get_ip(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))

        HOST = s.getsockname()[0]     # Endereco IP do Servidor
        PORT = "5000"                 # Porta que o Servidor esta

        return HOST, PORT




# instancia=Tk()
# servidor_interface(instancia)
# instancia.mainloop()
