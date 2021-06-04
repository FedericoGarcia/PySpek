from matplotlib.ticker import Formatter
import numpy as np
import matplotlib.pyplot as plt
import miniaudio as audio

from pyspek.analysis.pcm import GenerateTimeArray, ExtractChannelArray

audio_file_path = "pyspek/music.wav"
audio_file = audio.decode_file(audio_file_path)

x_axis = GenerateTimeArray(DecodedSoundFile = audio_file)
y1_axis = ExtractChannelArray(channel = 1, DecodedSoundFile = audio_file)
y2_axis = ExtractChannelArray(channel = 2, DecodedSoundFile = audio_file)

plt.figure()
plt.subplot(2, 1, 1*1)
plt.plot(x_axis, y1_axis)
plt.subplot(2, 1, 2*1)
plt.plot(x_axis, y2_axis)
#plt.show()
