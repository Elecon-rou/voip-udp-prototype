import pickle

import base64
from Crypto import Random
from Crypto.Cipher import AES

def parse_data(data,passwd):
	try:
		frame = pickle.loads(data)
	except:
		return data
	else:
		aes = AES.new(base64.b32encode(passwd.encode()), AES.MODE_CFB, frame['iv'])
		msg = pickle.loads(aes.decrypt(frame['msg']))
		return msg['text']

def pack_data(text,passwd):
	iv = Random.new().read(16)
	aes = AES.new(base64.b32encode(passwd.encode()), AES.MODE_CFB, iv)
	msg = {
		'text' : text,
		'magic'	: b'\x00\x88'
	}
	frame = {
		'iv' : iv,
		'msg' : aes.encrypt(pickle.dumps(msg))
	}
	return pickle.dumps(frame)