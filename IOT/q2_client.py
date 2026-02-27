import socket 
import threading

HOST='0.0.0.0'
PORT=12345 

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

def receive():
    while True:
        print(client.recv(1024).decode())

threading.Thread(target=receive).start()
while True:
    client.send(input().encode())