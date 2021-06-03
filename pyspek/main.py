from matplotlib.ticker import Formatter
import numpy as np
import matplotlib.pyplot as plt
import miniaudio as audio

audio_file_path = "pyspek/music.wav"
audio_file = audio.decode_file(audio_file_path)

def ExtractChannelArray(channel: int, DecodedSoundFile: audio.DecodedSoundFile) -> np.ndarray:
    if channel < 1:
        raise Exception("The selected channel number must be 1 or greater.")
    if channel > DecodedSoundFile.nchannels:
        raise Exception("The number of the selected channel exceeds the existing number of channels.")
        
    samples_per_channel = DecodedSoundFile.num_frames
    channel_array = np.zeros(samples_per_channel)
    index = 0
    for sample in range(channel - 1, samples_per_channel, channel):
        channel_array[index] = DecodedSoundFile.samples[sample]
        index = index + 1
    return channel_array

def GenerateTimeArray(DecodedSoundFile: audio.DecodedSoundFile) -> np.ndarray:
    num_frames = DecodedSoundFile.num_frames
    sample_rate = DecodedSoundFile.sample_rate
    time_array = np.zeros(num_frames)
    for index in range(num_frames):
        time_array[index] = index / sample_rate # in seconds
    return time_array

x_axis = GenerateTimeArray(DecodedSoundFile = audio_file)
y1_axis = ExtractChannelArray(channel = 1, DecodedSoundFile = audio_file)
y2_axis = ExtractChannelArray(channel = 2, DecodedSoundFile = audio_file)

plt.figure()
plt.subplot(2, 1, 1*1)
plt.plot(x_axis, y1_axis)
plt.subplot(2, 1, 2*1)
plt.plot(x_axis, y2_axis)
plt.show()