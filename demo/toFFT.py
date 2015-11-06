import glob
import matplotlib.pyplot as plt
from scipy.io import wavfile # get the api
from scipy.fftpack import fft
from pylab import *

def f(filename):
    fs, data = wavfile.read(filename) # load the data
    a = data.T[0] # this is a two channel soundtrack, I get the first track
    b=a#[(ele/2**8.)*2-1 for ele in a] # this is 8-bit track, b is now normalized on [-1,1)
    fs = fft(b) # create a list of complex number
    f = np.arange(0,len(fs)/2)  # you only need half of the fft list
    #plt.plot(abs(c[:(d-1)]),'r')
    #plt.magnitude_spectrum(abs(c[:(d-1)]), Fs=11025, scale='linear')

    plt.subplot(2, 1, 1)
    plt.plot(b)

    plt.subplot(2, 1, 2)
    plt.plot(f, abs(fs[:len(fs)/2]))
    plt.show()
    #savefig(filename+'.png',bbox_inches='wide')

#files = glob.glob('./*.wav')
#for ele in files:
f('E-Moll.wav')
#quit()
