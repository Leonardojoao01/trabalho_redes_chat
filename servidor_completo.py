from tkinter import *
#import thread
#import threading
#from threading import Thread
import _thread
import socket
import json
import re
import string

from servidor import *



class servidor_interface(Thread):
    subject_list = ""
    lista_clientes = []
    ip_clientes = []
    list_ips = []
    list_ports = []
    list_port_rem = []
    list_users = []
    def __init__(self, root=None):

        scrollbar = Scrollbar(root)

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

                # Mostra a parte das conversas
        #self.subject = Label(self.terceiroContainer, text="", bg="grey", width=90, height=20)
        #self.subject.pack(padx=10, side=LEFT)

        self.subject = Listbox(self.terceiroContainer, yscrollcommand=scrollbar.set, bg="grey", width=90, height=20)

        self.subject.pack(side=LEFT, fill=BOTH)
        scrollbar.config(command=self.subject.yview)

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



        #_thread.start_new_thread(self.serv, "JUCSA")

        _thread.start_new_thread(self.serv, tuple(["null","null"]))

        root.mainloop()

        #self.set_text("juca", self.conversa)

    def set_subject(self):

        subject_all = ""

        subject_field = self.nome.get()

        self.subject_list.append(subject_field+"\n")

        for subject_unique in self.subject_list:
             subject_all = subject_all + subject_unique #+ "\n"

        self.subject['text'] = subject_all

    def serv(self, juca1, juca2):
        #--------------------------Pega o IP local da máquina-------------------
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('google.com', 0))

        HOST = s.getsockname()[0]              # Endereco IP do Servidor
        PORT = 5000                            # Porta que o Servidor esta
        #-----------------------------------------------------------------------

        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # Reconect, utilizada
                                                    # quando a conecção n foi finalizada

        orig = (HOST, PORT)

        tcp.bind(orig)
        tcp.listen(1)

        while True:                     # Cria duas THREADS, SOCKET
            con, cliente = tcp.accept()
            _thread.start_new_thread(self.conectado, tuple([con, cliente]))

        tcp.close()

      #--------Quando alguém conecta, fica vinculado a esse processo--------------
    def conectado(self, con, cliente):
        print("Conectado por", cliente)     # Utilizado p/ verificar quem conecta

        self.list_ips.append(cliente[0])
        self.list_port_rem.append(cliente[1])
        print(self.list_ips, self.list_port_rem)

        checker = True;

        #=======================================================================

        while True:
            msg = con.recv(1024)            # Tamanho max da mensagem "(bytes)???"
            if not msg: continue

            #---------------Seta no CONVERSA o a mensagem recebida--------------
            self.subject_list=self.subject_list+"\n"+msg.decode()
            self.subject_list=msg.decode()
            self.subject.insert(0, self.subject_list)   # Insere o texto no campo
            #-------------------------------------------------------------------

            msg_desc = json.loads(msg.decode())

            if checker:                   # Usado para salvar a porta do cliente
                self.list_ports.append(msg_desc["port"])
                self.list_users.append(msg_desc["mensagem"])
                checker=False
            else:
            #======CHAMAR FUNÇÃO P/ ENVIAR MENSAGEM========
                self.connect_server(msg_desc["host"],msg_desc["port"],cliente[1],msg_desc["mensagem"],msg_desc["destinatario"])
            #==============================================

        print("Finalizando conexao do cliente", cliente)

        # Encontra a posicao da PORT, assim o indice é igual em todas as listas
        posicao = self.list_port_rem.index(cliente[1])

        self.list_ips.pop(posicao)
        self.list_ports.pop(posicao)
        self.list_port_rem.pop(posicao)
        self.list_users.pop(posicao)
        #-----------------------------------------------------------------------

        print(self.list_ips, self.list_port_rem, self.list_ports)

        con.close()
        _thread.exit()



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

    #-----------------------Enviar mensagens para vários---------------------------#
    def connect_server(self, host, port, port_un,text, dest):

        #print("JUCA", host, port, text)
        pos_port = 0;

        if dest == "all":

            for env_host in self.list_ips:
                print("ENV IP:", env_host, self.list_ports)
                posicao = self.list_port_rem.index(port_un)
                #pos_port =

                try:
                    HOST = str(self.list_ips[posicao])    # Endereco IP do Servidor
                    #PORT = int(self.list_ports[posicao])                 # Porta que o Servidor esta
                    PORT = int(self.list_ports[pos_port])
                    #print("HOST:PORT:TEXT", HOST, PORT, text)

                    tcp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    dest2 = (HOST, PORT)
                    tcp2.connect(dest2)
                    tcp2.send(text.encode())

                except:
                    print("ERRO DE ENVIO")

                pos_port = pos_port+1
        else:
            posicao = self.list_users.index(dest)
            try:
                HOST = str(self.list_ips[posicao])
                PORT = int(self.list_ports[pos_port])
                tcp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dest2 = (HOST, PORT)
                tcp2.connect(dest2)
                tcp2.send(text.encode())
            except:
                print("ERRO DE ENVIO")


    def ip_and_port(self, cliente):
        #print("CLI", type(cliente))
        #print("CLI", cliente[0])
        #print("CLI", cliente[1])
        # ip_juca = ""
        # po_juca = ""
        # cont = 0
        # min_host = str(cliente).find("'")+1
        # max_host = str(cliente).find(",")-2
        # print(min_host, max_host)
        #
        # min_port = str(cliente).find(" ")+1
        # max_port = str(cliente).find(")")-1
        #
        # print("NUN: ",len(cliente))
        #
        # for letra in cliente:
        #     if cont >= min_host and cont <= max_host :
        #         ip_juca = ip_juca + letra
        #     if cont >= min_port and cont <= max_port :
        #         po_juca = po_juca + letra
        #
        #     cont=cont+1
        #     print(cont)
        #
        # print("IP:PORT", ip_juca, po_juca)

        return cliente[0],cliente[1]



#---------------------------------------#

root = Tk()
servidor_interface(root)

#jucaaa = servidor_interface(root)
#_thread.start_new_thread(self.serv, "JUCSA")


# instancia=Tk()
# servidor_interface(instancia)
# instancia.mainloop()
