import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('google.com', 0))

HOST = s.getsockname()[0]     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

#print(HOST,PORT)
tcp.connect(dest)

print('Para sair use CTRL+X\n')
msg = input()

#print(type(msg))

while msg != '\x18':

	msg = "'{\"mensagem\": \"" + msg + "\", " + "\"host\": \"" + str(HOST) + "\", " + "\"port\": \"" + str(PORT) + "\"}'"

	tcp.send(msg.encode())
	msg = input()
tcp.close()
