#https://www.youtube.com/watch?v=u4kr7EFxAKk&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=82

# SOcket prgramming in python

# this is server socket

import socket

s=socket.socket()
print('socket created')
s.bind(('localhost',9999)) # this is used to connect server with client

s.listen(3)  # this means we can only connect 3 clients
print("waiting for connection ")

while True:
    c,addr = s.accept()
    name=c.recv(1024,).decode()
    print("connected with " ,addr,name )

    c.send(bytes('welcome to socket programming ','utf-8'))# we need to send it in byte format






