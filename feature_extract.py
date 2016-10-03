import numpy as np
import pyedflib
import matplotlib.pyplot as plt
from numpy import fft

f = pyedflib.EdfReader("S01-01-25.09.2016.10.21.24.edf")
n = f.signals_in_file
signal_labels = f.getSignalLabels()
sigbufs = np.zeros((n, f.getNSamples()[0]))

for i in np.arange(n):
	sigbufs[i, :] = f.readSignal(i)
	
print (sigbufs);
for i in np.arange(2:15):
	plt.plot(sigbufs[i])
	plt.show()

for i in np.arange(2:15):
	spectrum[i]=fft.fft(sigbufs[i])
	freq=fft.fftfreq(len(spectrum[i]))
	plt.plot(freq,abs(spectrum))
	plt.show()


raw_input()
#here we have 184s equivalent to 23552
#sampling frequency 128 Hz