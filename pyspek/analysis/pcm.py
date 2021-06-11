import miniaudio
import numpy

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

'''
def NormalizeSampleArray(sample: numpy.ndarray) -> numpy.ndarray:
    return sample / numpy.linalg.norm(sample)
'''

def MultichannelArray(DecodedSoundFile: miniaudio.DecodedSoundFile):
    number_of_channels = DecodedSoundFile.nchannels
    samples_per_channel = DecodedSoundFile.num_frames
    multichannel = numpy.zeros(shape = (number_of_channels, samples_per_channel))
    for index in range(number_of_channels):
        multichannel[index] = ExtractChannelArray(index + 1, DecodedSoundFile)
    return multichannel

def ConvertToMono(DecodedSoundFile: miniaudio.DecodedSoundFile) -> numpy.ndarray:
    multichannel = MultichannelArray(DecodedSoundFile)
    return numpy.sum(multichannel / DecodedSoundFile.nchannels, axis = 0)