import alsaaudio
from opuslib import Encoder, Decoder, api

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(2)
inp.setrate(48000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(960)

outp = alsaaudio.PCM(alsaaudio.PCM_PLAYBACK)
outp.setchannels(2)
outp.setrate(48000)
outp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
outp.setperiodsize(960)

e = Encoder(48000,2,api.constants.APPLICATION_AUDIO)

d = Decoder(48000,2)

while True:
	len, pcm = inp.read()
	encoded = e.encode(pcm ,960)
	decoded = d.decode(encoded, frame_size=960)
	outp.write(decoded)