import numpy as np
import miniaudio as audio

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