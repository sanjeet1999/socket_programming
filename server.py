import socket 
s = socket.socket()
s.bind(("localhost",9999))
s.listen(4)
print("wating for the connections")
while True:
    c,addr = s.accept()
    name = c.recv(1024).decode()
    print("i connected to add",(addr,name))

    c.send(bytes(f"welcome to sanjeet's website!!! {name}",'utf-8'))
    c.close