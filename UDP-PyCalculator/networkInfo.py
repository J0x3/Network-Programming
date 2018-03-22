#class file for network information for client/server
#UDP implementation
import socket
class UDP:
	PORT1 = 5005 #port option 1
	PORT2 = 5006 #port option 2
	PORT3 = 5007 #port option 3
	LHOST_IP = "" #Set host IP of client!
	RHOST_IP = "" #Client needs to know/set remote server IP

	#server can auto generate IP
	def get_ip():
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		try:
			s.connect(('10.255.255.255', 1))
			SERVER_IP = s.getsockname()[0]
		except:
			SERVER_IP = '127.0.0.1'
		finally:
			s.close()
		return SERVER_IP
	
	SERVER_IP = get_ip() #server IP auto
	#SERVER_IP = '127.0.0.1' #manual assignment

