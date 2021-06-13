import miniaudio
import numpy
import pyspek.dsp.core.audio

def decode_file(audio_file_path = str) -> pyspek.dsp.core.audio.Data:
    audio_file = miniaudio.decode_file(audio_file_path)
    pcm_samples = audio_file.samples
    bit_depth = 16
    sample_rate = 44100
    channels_count = audio_file.nchannels
    channel_samples_count = audio_file.num_frames

    samples = numpy.zeros(shape = (channels_count, channel_samples_count))
    
    for sample in range(channel_samples_count):
        for channel in range(channels_count):
            samples[channel][sample] = pcm_samples[channel*sample]

    return pyspek.dsp.core.audio.Data(bit_depth, sample_rate, samples)