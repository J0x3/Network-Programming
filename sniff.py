#Linux sniffer
#Must been run as root (sudo pyton sniff.py)
#TODO: implement read packet data
import socket, sys
from struct import *

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

while True: #acquire data and split packet data
   packet = s.recvfrom(65565)               #data recv
   #print(packet) #debug
   packet = packet[0]                       #packet string
   ip_header = packet[0:20]                 #ip header characters
   iph = unpack('!BBHHHBBH4s4s' , ip_header)#unpack header
   #print(iph) #debug
   version_ihl = iph[0]                     #version number
   version = version_ihl >> 4               #conversion 
   ihl = version_ihl & 0xF                  #conversion
   iph_length = ihl * 4                     #header length
   ttl = iph[5]                             #time to live
   protocol = iph[6]                        #protocol type
   s_addr = socket.inet_ntoa(iph[8])        #source
   d_addr = socket.inet_ntoa(iph[9])        #destination

   #print data
   print("Version: " + str(version) + " IP Header Length: " + str(ihl) + " TTL: " + str(ttl) + " Protocol: " + str(protocol) + " Source Addr: " + str(s_addr) + " Destination: " + str(d_addr)) 

   #p_header = packet[20:]                 #ip header characters
   #data = unpack('!BBHHHBBH4s4s' , p_header)
   #print("Data: " + data)
