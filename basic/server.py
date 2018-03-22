#Server
import socket
import subprocess

UDP_IP = "127.0.0.1" #change this
UDP_PORT = 5555      #can change

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
   data, addr = sock.recvfrom(1024)
   print("received message: ", data.decode())
