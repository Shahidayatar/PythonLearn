# this is client side
# always run the server first
import socket

c=socket.socket()# you can mention two arguments 1.ipv4 or ipv6(ip address) 2. type of connection tcp  or udp

c.connect(('localhost',9999))#we connect here not bind it because it is clent

name= input("enter your name")
c.send(bytes(name,'utf-8'))
print(c.recv(1024).decode())# we received from servers