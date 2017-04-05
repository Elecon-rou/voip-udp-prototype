import alsaaudio
import sys
from opuslib import Encoder, Decoder, api

# 8k 12k 16k 24k 48k
rate = 8000
# 40 80 160 320 640 960
period = 40
channels = 1

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(channels)
inp.setrate(rate)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(period)

outp = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
outp.setchannels(channels)
outp.setrate(rate)
outp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
outp.setperiodsize(period)

e = Encoder(rate,channels,api.constants.APPLICATION_VOIP)
d = Decoder(rate,channels)

while True:
	len, pcm = inp.read()
	encoded = e.encode(pcm, period)
	print(sys.getsizeof(encoded))
	decoded = d.decode(encoded, frame_size=period)
	outp.write(decoded)

