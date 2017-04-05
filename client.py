import socket
import sys
import ctypes
import alsaaudio

from common import parse_data, pack_data


passwd = 'test_passphrase'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 4242)

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(2)
inp.setrate(16000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(1024)

while True:
	len, data = inp.read()
	sock.sendto(pack_data(data, passwd), server_address)

#data, address = sock.recvfrom(1024)
#print(parse_data(data,passwd))

sock.close()