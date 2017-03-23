import socket
import sys
import base64
import pickle
from Crypto import Random
from Crypto.Cipher import AES

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('213.108.170.103', 4242)

iv = Random.new().read(16)
aesenc = AES.new(base64.b32encode('test_passphrase'.encode()), AES.MODE_CFB, iv)
aesdec = AES.new(base64.b32encode('test_passphrase'.encode()), AES.MODE_CFB, iv)

msg = {
	'text' : 'LOREM IPSUM DOLOR SIT AMET',
	'magic'	: b'\x00\x88'
}

frame = {
	'iv' : iv,
	'msg' : aesenc.encrypt(pickle.dumps(msg))
}

rcv_frame = pickle.loads(pickle.dumps(frame))
rcv_msg = pickle.loads(aesdec.decrypt(rcv_frame['msg']))

if rcv_msg['magic'] == b'\x00\x88':
	print(rcv_msg['text'])
"""
sent = sock.sendto(data, server_address)
print(sock.recvfrom(1024))
sock.close()
"""