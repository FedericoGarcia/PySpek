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
    total_samples_count = channels_count * channel_samples_count

    samples = numpy.zeros(shape = (channels_count, channel_samples_count))

    for sample in range(total_samples_count):
        samples[sample % channels_count][numpy.floor(sample / channels_count)] = pcm_samples[sample]

    return pyspek.dsp.core.audio.Data(bit_depth, sample_rate, samples)