import socket
import sys
import time
s=socket.socket()
host=socket.gethostname()
print("server will be start o host",host)
port=8080
s.bind((host,port))
print("")
print("server done Binding to the host port successfully")
print("")
s.listen(1)
conn,addr=s.accept()
print(addr,"has connected to the server")
print("")
message=input(str(">>"))
while 1:
    message=message.encode()
    conn.send(message)

    print("Message Hasbeen send")
    print("")
    incoming_message=conn.recv(1024)
    incoming_message=incoming_message.decode()
    print("client",incoming_message)
    print("")
