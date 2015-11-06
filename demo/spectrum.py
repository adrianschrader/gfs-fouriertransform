import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile

dt = 1.0/11025
Fs = 1/dt
t = np.arange(0, 1, dt)
nse = np.random.randn(len(t))
r = np.exp(-t/(dt*5))

cnse = np.convolve(nse, r)*dt
cnse = cnse[:len(t)]
s = 0.1*np.sin((2*np.pi*500)*t) + 0.09*np.sin((2*np.pi*600)*t) + 0.08*np.sin((2*np.pi*705)*t) + 0.07*np.sin((2*np.pi*1000)*t) + 1000*cnse

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

wavfile.write("output.wav", len(s)/1, s)

#plt.subplot(2, 1, 2)
#plt.magnitude_spectrum(s, Fs=Fs)

plt.show()
