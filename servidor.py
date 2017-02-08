import socket
import _thread
from tkinter import *
from threading import Thread


#from servidor_interface import *

class servidor(Thread):

    juca = None
    def __init__(self, obj):
        #--------------------------Pega o IP local da máquina-------------------
        Thread.__init__(self)
        self.juca = obj
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

        while True:                     # Cria duas THREADS, SOCKET e ANALIZADOR
            con, cliente = tcp.accept()
            _thread.start_new_thread(self.conectado, tuple([con, cliente]))

        tcp.close()

    #----------------------Função de comunicação, por SOCKET--------------------
    def conectado(self, con, cliente):
        print("Conectado por", cliente)     # Utilizado p/ verificar quem conecta

        while True:
            msg = con.recv(1024)            # Tamanho max da mensagem "(bytes)???"
            if not msg: break

            self.juca.set_text(msg.decode(),"subject")

            print(msg.decode())

        print("Finalizando conexao do cliente", cliente)
        con.close()
        _thread.exit()
