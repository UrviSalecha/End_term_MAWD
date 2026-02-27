#Multi Client Chat System using TCP and Multi-Threading
# TCP Server
import socket
import threading

HOST='0.0.0.0'
PORT=12345

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
clients=[]

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            msg=client.recv(1024)
            broadcast(msg)
        except:
            clients.remove(client)
            client.close()
            break
print("Server is listening.....")
while True:
    client,addr=server.accept()
    print("connected:",addr)
    clients.append(client)
    thread=threading.Thread(target=handle, args=(client,))
    thread.start()        
    