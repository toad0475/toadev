import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt


sr, data = sio.wavfile.read('UI_CheckButton.wav')

data = data / 2.**15
t = np.linspace(0, len(data)/float(sr), len(data))

plt.plot(t,data)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.show()
