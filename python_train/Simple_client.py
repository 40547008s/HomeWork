import socket

Host = "0.0.0.0"
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host,PORT))

while True:
    cmd = input("Please input msg:")
    s.send(bytearray(cmd,'utf-8'))
    data = s.recv(1024)
    print("server send : %s"%(data))