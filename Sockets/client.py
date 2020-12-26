import socket
HEADER = 64
PORT = 5050 
FORMAT = 'utf-8'
DISCONNCET_MESSAGE = "!DISCONNECT"
SERVER = "10.0.0.17"
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)