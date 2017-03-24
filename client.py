import socket
import sys

from common import parse_data, pack_data

passwd = 'test_passphrase'

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 4242)

sock.sendto(pack_data('LOREM IPSUM DOLOR SIT AMET',passwd), server_address)

data, address = sock.recvfrom(1024)
print(parse_data(data,passwd))

sock.close()