#python 2 udp client
#Author:Itzel Gonzalez//Richard Cave//Joseph Osborne//et al. CSV19
#make sure to check network settings in networkInfo
#wont run if LHOST and RHOST not specified
import select
import socket
#get IP and PORT from NetworkClass
from networkInfo import UDP

print "Chose operator then digits"
print "Ex: \"+ 1 2\" or \"* 7 3\""
msg = raw_input("Enter a caclutation: ")

#send to server
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(msg, (UDP.RHOST_IP, UDP.PORT1))

#listen on local
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind((UDP.LHOST_IP, UDP.PORT1))

sock2.setblocking(0)

wait = 5
sentinel = True
while sentinel:
	ready = select.select([sock2], [], [], 5)
	if ready[0]:
		data, addr = sock2.recvfrom(1024)
		print addr
		print data
		sentinel = False
	else:
		wait -= 1
