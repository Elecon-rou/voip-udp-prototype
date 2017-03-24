import socket
import sys
import time

from common import parse_data

class client:
	def __init__(self, address, timestamp):
		self.addr = address
		self.time = timestamp

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',4242))

clients=[]

while True:
	data, address = sock.recvfrom(1024)

	print(parse_data(data,'test_passphrase'))

	t = int(time.time())
	i = 0
	new = 1
	while i < len(clients): # Iterate clients table
		if clients[i].addr == address: # Update sender's timestamp
			clients[i].time = t
			new = 0 # Sender still presents in clients table
		else:
			sock.sendto(data, clients[i].addr) # Retranslate data to others
		if t - clients[i].time > 8: # Unsubscribe clients with no activity
			clients.pop(i)
		i += 1
	if new: # Subscribe sender
		clients.append(client(address,t))