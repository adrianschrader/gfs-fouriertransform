import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile

fs, data = wavfile.read("E-Moll.wav") # load the data
s = data # this is a two channel soundtrack, I get the first track
#s=[(ele/2**8.)*2-1 for ele in a]
t = np.arange(0,len(s)/11025.0, 1/11025.0)

print(data)

fs = fft(s)
f = np.arange(0,len(fs)/2)

plt.subplot(2, 1, 1)
plt.plot(t, s)
plt.xlabel("Zeit (s)")
plt.ylabel("Auslenkung")

plt.subplot(2, 1, 2)
plt.plot(f, abs(fs[:len(fs)/2]))
plt.xlabel("Frequenz (Hz)")
plt.ylabel("Amplitude")

#plt.subplot(2, 1, 2)
#plt.magnitude_spectrum(s, Fs=Fs)

plt.show()
