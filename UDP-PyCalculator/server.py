#server uses python 2
#Author:Itzel Gonzalez//Richard Cave//Joseph Osborne//et al. CSV19
#check networkInfo.py for networkng details
import socket
import subprocess
#UDP class, network details 
from networkInfo import UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP.SERVER_IP, UDP.PORT1)) 

print "Server IP: " + UDP.SERVER_IP

while True:	
	print "~ Waiting ~"	
	pop = True
	while pop == True:	
		data, addr = sock.recvfrom(1024)
		print addr
		print "Received Message: ", data
		calc = data.split(" ")	
		msg = ""	
		result = 0
		#data catch
		stop = raw_input("Press Enter to process input....")
		if(stop == ""):	
			#calculations
			if(calc[0] == '+'):
				for i in calc:
					if(i != '+'):
						result = result + int(i)
					msg = str(result)	
			if(calc[0] == '*'):
				result = 1
				for i in calc:
					if(i != '*'):
						result *= int(i)
					msg = str(result)
			if(calc[0] == '-'):	
				result = int(calc[1])
				for i in calc[2:]:
					result -= int(i)
				msg = str(result)      
			if(calc[0] == '/'):
				result = int(calc[1])
				for i in calc[2:]:
					result /= int(i)
				msg = str(result)      

			#send message back
			sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			sock2.sendto(msg, (addr[0], UDP.PORT1))
			print "#Sent#"
			pop = False
