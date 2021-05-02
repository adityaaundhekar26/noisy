import IPython
from scipy.io import wavfile
import noisereduce as nr
import soundfile as sf
from noisereduce.generate_noise import band_limited_noise
import matplotlib.pyplot as plt
import urllib.request
import numpy as np
import io


data, rate = sf.read("/content/SY-IC-A 13.wav")
data = data

IPython.display.Audio(data=data, rate=rate)

fig, ax = plt.subplots(figsize=(20,3))
ax.plot(data)

