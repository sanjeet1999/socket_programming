import socket 
c = socket.socket()
c.connect(("localhost",9999))
name = input("Enter your name ")
c.send(bytes(f"{name}",'utf-8'))
print(c.recv(1024).decode("utf-8"))