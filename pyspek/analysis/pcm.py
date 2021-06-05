import numpy
import miniaudio

def ExtractChannelArray(channel: int, DecodedSoundFile: miniaudio.DecodedSoundFile) -> numpy.ndarray:
    if channel < 1:
        raise Exception("The selected channel number must be 1 or greater.")
    if channel > DecodedSoundFile.nchannels:
        raise Exception("The number of the selected channel exceeds the existing number of channels.")
        
    samples_per_channel = DecodedSoundFile.num_frames
    number_of_channels = DecodedSoundFile.nchannels
    channel_array = numpy.zeros(samples_per_channel)
    index = 0
    for sample in range(channel - 1, samples_per_channel*number_of_channels, number_of_channels):
        channel_array[index] = DecodedSoundFile.samples[sample]
        index = index + 1
    return channel_array

def GenerateTimeArray(DecodedSoundFile: miniaudio.DecodedSoundFile) -> numpy.ndarray:
    samples_per_channel = DecodedSoundFile.num_frames
    sample_rate = DecodedSoundFile.sample_rate
    time_array = numpy.zeros(samples_per_channel)
    for index in range(samples_per_channel):
        time_array[index] = index / sample_rate
    return time_array
