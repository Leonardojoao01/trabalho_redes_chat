from tkinter import *
#import thread
#import threading
#from threading import Thread
import _thread
import socket
import json
import re
import string
import time

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

        # Instancia uma thread para receber as mensagens dos clientes
        _thread.start_new_thread(self.serv, tuple(["null","null"]))

        root.mainloop()

    def set_subject(self):

        #subject_field = self.nome.get()
        for env_host in self.list_port_rem:
            posicao = self.list_port_rem.index(env_host)

            msg = '{"mensagem":  "'+str(self.nome.get())+'", "destinatario": "'+self.list_users[posicao]+'", "remetente": "'+"SERVER"+'"}'

            try:
                HOST = str(self.list_ips[posicao])
                PORT = int(self.list_ports[posicao])
                tcp3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcp3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                dest3 = (HOST, PORT)
                tcp3.connect(dest3)
                tcp3.send(msg.encode())
                tcp3.close()

            except Exception as inst:
            	print(inst)
            	print("ERRO DE ENVIO")




        #self.subject_list.append(subject_field+"\n")

        #for subject_unique in self.subject_list:
        #     subject_all = subject_all + subject_unique #+ "\n"

        #self.subject['text'] = subject_all

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

        while True:         # Cria THREAD para ficar em um loop até cliente se desconectar
            con, cliente = tcp.accept()
            _thread.start_new_thread(self.conectado, tuple([con, cliente]))

        tcp.close()

      #--------Quando alguém conecta, fica vinculado a esse processo--------------
    def conectado(self, con, cliente):
        print("Conectado por", cliente)
        # Cliente[0] = IP do cliente conectado
        # Cliente[1] = ID da conexão

        self.list_ips.append(cliente[0])
        self.list_port_rem.append(cliente[1])
        print(self.list_ips, self.list_port_rem)

        checker = True;

        #=======================================================================

        while True:
            msg = con.recv(1024)            # Tamanho max da mensagem "(bytes)???"
            if not msg: break

            #---------------Seta no campo CONVERSA a mensagem recebida--------------
            self.subject_list=self.subject_list+"\n"+msg.decode()   # Concatena a mensagem alterior com a nova
            self.subject_list=msg.decode()              # Leitura da mensagem
            self.subject.insert(0, self.subject_list)   # Insere o texto no campo
            # OBS: Não foi colocado o "msg.decode()" direto na função insert, pois gera um erro
            #-------------------------------------------------------------------

            msg_desc = json.loads(msg.decode())

            # Utilizado para entrar somente uma unica vez a cada novo cliente conectado
            # Função principal desse trecho do código é conectar diversos clientes
            # no mesmo computador, pois o IP é o mesmo e devemos realizar a analogia
            # entre as tabelas. Assim, diferenciamos pelo id da conexão cliente[1]
            # realizando a analogia com a mesma posicao de outra tabela referente a porta
            # dos clientes
            if checker:
                self.list_ports.append(msg_desc["port"])
                self.list_users.append(str(msg_desc["mensagem"]))
                self.set_text(self.list_users, self.users)
                self.send_all()
                #self.connect_server("192.168.15.9","4000",cliente[1],"juca","all")

                checker=False
            else:
                self.connect_server(msg_desc["host"],msg_desc["port"],cliente[1],msg_desc["mensagem"],msg_desc["destinatario"],cliente[1])
            #==============================================

        print("Finalizando conexao do cliente", cliente)
        # Encontra a posicao na tabela de id de conexao(cliente[1])
        # Dessa forma é possivel remover todos os dados referente ao mesmo cliente
        # em todas as listas
        posicao = self.list_port_rem.index(cliente[1])

        self.list_ips.pop(posicao)          # IP do cliente
        self.list_ports.pop(posicao)        # PORTA do cliente
        self.list_port_rem.pop(posicao)     # ID de conexão
        self.list_users.pop(posicao)        # NOME do usuário conectado
        self.set_text(self.list_users, self.users)
        #-----------------------------------------------------------------------
        self.send_all()

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
    #-----------------------Envia mensagens a todos-----------------------------
    def send_all(self):
        for env_host in self.list_port_rem:
            print(self.list_port_rem)
            posicao = self.list_port_rem.index(env_host)
            #print(str(env_host) + "-" + str(posicao)+ "user"+self.list_users[posicao])
            #print("ENV IP:", self.list_ips[posicao], self.list_ports[posicao])

            users_msg = ' '.join(map(str, self.list_users))#str(users) + users_msg
            #
            msg = '{"mensagem":  "'+"!TRUE!"+'", "destinatario": "'+"all"+'", "remetente": "'+users_msg+'"}'
            #print(msg)

            try:
	            HOST = str(self.list_ips[posicao])
	            print("host - " + HOST)    # Endereco IP do Servidor
	            PORT = int(self.list_ports[posicao])
	            assert(PORT)
	            #PORT=4100
	            print("porta - \n" +str(PORT))
	            #tcp3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	            #tcp3 = socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	            tcp3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	    tcp3.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	            dest3 = (HOST, PORT)
	            print(dest3)
	            tcp3.connect(dest3)
	            tcp3.send(msg.encode())
	            #print(tcp3.send(msg.encode()))
	            tcp3.close()

            except Exception as inst:
            	print(inst)
            	print("ERRO DE ENVIO")

    #===========================================================================
    #-----------------------Enviar mensagens para vários-----------------------#

    def connect_server(self, host, port, port_un,text, dest, id_remetente):

        #print("JUCA", host, port, text)
        pos_port = 0;

        nome_rem = str(self.list_users[self.list_port_rem.index(id_remetente)])
        #("NOME_DEST:", nome_rem)
        #pos_rem = self.list_port_rem.index(cliente[1])

        if dest == "all":

            for env_host in self.list_ips:
                print("ENV IP:", env_host, self.list_ports)
                posicao = self.list_port_rem.index(port_un)
                #pos_port =

                msg = '{"mensagem":  "'+text+'", "destinatario": "'+"all"+'", "remetente": "'+nome_rem+'"}'


                try:
                    HOST = str(self.list_ips[posicao])    # Endereco IP do Servidor
                    #PORT = int(self.list_ports[posicao])                 # Porta que o Servidor esta
                    PORT = int(self.list_ports[pos_port])
                    #print("HOST:PORT:TEXT", HOST, PORT, text)

                    tcp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    dest2 = (HOST, PORT)
                    tcp2.connect(dest2)

                    tcp2.send(msg.encode())

                except:
                    print("ERRO DE ENVIO")

                pos_port = pos_port+1
        else:

            posicao = self.list_users.index(str(dest))

            #print("DEST:POS:PORT ", dest, posicao)
            msg = '{"mensagem":  "'+text+'", "destinatario": "'+self.list_users[posicao]+'", "remetente": "'+nome_rem+'"}'
            #print("MSN: ", msg)
            try:
                HOST = str(self.list_ips[posicao])
                PORT = int(self.list_ports[posicao])
                tcp2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                dest2 = (HOST, PORT)
                tcp2.connect(dest2)
                tcp2.send(msg.encode())
            except:
                print("ERRO DE ENVIO")

#---------------------------------------#

root = Tk()
servidor_interface(root)

#jucaaa = servidor_interface(root)
#_thread.start_new_thread(self.serv, "JUCSA")


# instancia=Tk()
# servidor_interface(instancia)
# instancia.mainloop()
