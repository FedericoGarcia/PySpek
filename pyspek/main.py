import matplotlib
import miniaudio
import numpy
import pyspek

audio_file_path = "pyspek/music.wav"
audio_file = miniaudio.decode_file(audio_file_path)

x_axis = pyspek.analysis.pcm.GenerateTimeArray(DecodedSoundFile = audio_file)
y1_axis = pyspek.analysis.pcm.ExtractChannelArray(channel = 1, DecodedSoundFile = audio_file)
y2_axis = pyspek.analysis.pcm.ExtractChannelArray(channel = 2, DecodedSoundFile = audio_file)

"""
matplotlib.pyplot.plt.figure()
matplotlib.pyplot.plt.subplot(2, 1, 1*1)
matplotlib.pyplot.plt.plot(x_axis, y1_axis)
matplotlib.pyplot.plt.subplot(2, 1, 2*1)
matplotlib.pyplot.plt.plot(x_axis, y2_axis)
matplotlib.pyplot.plt.show(block = True)
"""