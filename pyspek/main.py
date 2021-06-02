from matplotlib.ticker import Formatter
import numpy as np
import matplotlib.pyplot as plt
import miniaudio as audio

audio_file_path = "pyspek/music.wav"

audio_file = audio.decode_file(audio_file_path)

samples = audio_file.samples
nchannels = audio_file.nchannels

def ExtractChannelArray(channel, DecodedSoundFile):
    samples_per_channel = DecodedSoundFile.num_frames
    channel_array = np.zeros(samples_per_channel)
    index = 0
    for sample in range(channel - 1, samples_per_channel, channel):
        channel_array[index] = DecodedSoundFile.samples[sample]
        index = index + 1
    return channel_array

print(ExtractChannelArray(channel = 1, DecodedSoundFile = audio_file))
print(len(ExtractChannelArray(channel = 1, DecodedSoundFile = audio_file)))