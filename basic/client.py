#client
import socket
import re

UDP_IP = "127.0.0.1" #change this to server ip
UDP_PORT = 5555      #change this to server port
MESSAGE = input("Type Message: ")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE.encode(),(UDP_IP, UDP_PORT))
