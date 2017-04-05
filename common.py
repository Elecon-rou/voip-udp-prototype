import pickle
import queue
import threading
import base64
import alsaaudio
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
		return msg['data']

def pack_data(data,passwd):
	iv = Random.new().read(16)
	aes = AES.new(base64.b32encode(passwd.encode()), AES.MODE_CFB, iv)
	msg = {
		'data' : data,
		'magic'	: b'\x00\x88'
	}
	frame = {
		'iv' : iv,
		'msg' : aes.encrypt(pickle.dumps(msg))
	}
	return pickle.dumps(frame)

class playback_thread(threading.Thread):
	def __init__(self,buffer):
		threading.Thread.__init__(self)
		self.buffer = buffer
		self.outp = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
		self.outp.setchannels(2)
		self.outp.setrate(16000)
		self.outp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
		self.outp.setperiodsize(1024)
	def run(self):
		while True:
			self.outp.write(self.buffer.get())