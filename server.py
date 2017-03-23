import socket
import sys
import time

class client:
	def __init__(self, address, timestamp):
		self.addr = address
		self.time = timestamp

class fifo:
	def __init__(self):
		pass
	def pop:
		pass
	def push:
		pass

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0',4242))

clients=[]

while True:
	data, address = sock.recvfrom(1024)
	t = int(time.time())
	i = 0
	new = 1
	while i < len(clients):
		if clients[i].addr == address:
			clients[i].time = t
			new = 0
		else:
			sock.sendto(data, clients[i].addr)
		if t - clients[i].time > 8:
			clients.pop(i)
		i += 1
	if new:
		clients.append(client(address,t))
	print(data)
	print(clients)