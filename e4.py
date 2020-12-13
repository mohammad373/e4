# e4

# clant

import socket

s = socket.socket()
port = 8500
ip = '192.168.1.54'
s.connect((ip, port))
print('Connected')
while True:
    print(s.recv(1024).decode())
    message = input('Your Message : ')
    s.send(message.encode())
