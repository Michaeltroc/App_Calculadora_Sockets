import socket

HOST = '127.0.0.1'
PORT=65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Conexion establecida con el servidor')

while True:
    data = s.recv(1024).decode()
    if not data:
        break
    print('\n(Mensaje del servidor) ',data)
    mensaje_enviar = str(input())
    s.sendall(mensaje_enviar.encode())